import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Reward Intelligence | Almedia Concept",
    layout="wide"
)

df = pd.read_csv("data/reward_optimizer_output.csv")

# Theme styling
st.markdown("""
<style>
.stApp {
    background-color: #050505;
    color: #F5F5F5;
}
h1, h2, h3 {
    color: #D7FF3F;
}
[data-testid="stMetricValue"] {
    color: #D7FF3F;
}
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

st.title("Reward Dependency Intelligence System")
st.caption("Almedia-style incentive optimization engine for rewarded user acquisition platforms")

# Sidebar filters
st.sidebar.header("Filters")

country = st.sidebar.multiselect(
    "Country",
    options=df["country"].unique(),
    default=df["country"].unique()
)

device = st.sidebar.multiselect(
    "Device",
    options=df["device"].unique(),
    default=df["device"].unique()
)

source = st.sidebar.multiselect(
    "Acquisition Source",
    options=df["acquisition_source"].unique(),
    default=df["acquisition_source"].unique()
)

segment = st.sidebar.multiselect(
    "User Segment",
    options=df["segment"].unique(),
    default=df["segment"].unique()
)

filtered = df[
    (df["country"].isin(country)) &
    (df["device"].isin(device)) &
    (df["acquisition_source"].isin(source)) &
    (df["segment"].isin(segment))
]

# KPIs
total_current = filtered["reward_amount"].sum()
total_suggested = filtered["suggested_reward"].sum()
total_savings = filtered["estimated_savings"].sum()
savings_pct = (total_savings / total_current) * 100 if total_current > 0 else 0
avg_dependency = filtered["reward_dependency_score"].mean()

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Users Analysed", f"{len(filtered):,}")
col2.metric("Current Spend", f"€{total_current:,.0f}")
col3.metric("Optimized Spend", f"€{total_suggested:,.0f}")
col4.metric("Savings", f"€{total_savings:,.0f}")
col5.metric("Savings Rate", f"{savings_pct:.2f}%")

st.divider()

# Business insight box
st.subheader("Executive Insight")

st.markdown(f"""
### The system identifies **€{total_savings:,.0f}** in potential reward savings  
without applying a one-size-fits-all reward cut.

Instead, it segments users by reward dependency and recommends whether to:

- Keep the current reward
- Reduce reward by 20%
- Reduce reward by 40%

Average Reward Dependency Score: **{avg_dependency:.1f}/100**
""")

st.divider()

# Charts
colA, colB = st.columns(2)

with colA:
    st.subheader("Reward Recommendation Breakdown")
    rec_counts = filtered["recommendation"].value_counts().reset_index()
    rec_counts.columns = ["Recommendation", "Users"]

    fig1 = px.bar(
        rec_counts,
        x="Recommendation",
        y="Users",
        text="Users",
        title="Users by Reward Action",
        template="plotly_dark"
    )
    fig1.update_layout(
        paper_bgcolor="#050505",
        plot_bgcolor="#050505",
        font_color="#F5F5F5"
    )
    st.plotly_chart(fig1, width="stretch")

with colB:
    st.subheader("Reward Budget Optimization")
    spend_df = pd.DataFrame({
        "Category": ["Current Spend", "Optimized Spend", "Savings"],
        "Amount": [total_current, total_suggested, total_savings]
    })

    fig2 = px.bar(
        spend_df,
        x="Category",
        y="Amount",
        text="Amount",
        title="Spend Before vs After Optimization",
        template="plotly_dark"
    )
    fig2.update_layout(
        paper_bgcolor="#050505",
        plot_bgcolor="#050505",
        font_color="#F5F5F5"
    )
    st.plotly_chart(fig2, width="stretch")

st.divider()

colC, colD = st.columns(2)

with colC:
    st.subheader("Dependency Score by Segment")

    fig3 = px.box(
        filtered,
        x="segment",
        y="reward_dependency_score",
        title="Reward Dependency Distribution",
        template="plotly_dark"
    )
    fig3.update_layout(
        paper_bgcolor="#050505",
        plot_bgcolor="#050505",
        font_color="#F5F5F5"
    )
    st.plotly_chart(fig3, width="stretch")

with colD:
    st.subheader("Savings by Acquisition Source")

    source_savings = filtered.groupby("acquisition_source")["estimated_savings"].sum().reset_index()

    fig4 = px.pie(
        source_savings,
        names="acquisition_source",
        values="estimated_savings",
        title="Where Reward Savings Come From",
        template="plotly_dark"
    )
    fig4.update_layout(
        paper_bgcolor="#050505",
        plot_bgcolor="#050505",
        font_color="#F5F5F5"
    )
    st.plotly_chart(fig4, width="stretch")

st.divider()

st.subheader("High-Impact Users: Highest Reward Savings Opportunity")

top_users = filtered.sort_values("estimated_savings", ascending=False).head(25)

st.dataframe(
    top_users[
        [
            "user_id",
            "country",
            "device",
            "acquisition_source",
            "segment",
            "reward_amount",
            "suggested_reward",
            "estimated_savings",
            "reward_dependency_score",
            "recommendation"
        ]
    ],
    width="stretch"
)

st.divider()

st.subheader("Strategic Recommendation")

st.markdown("""
This dashboard suggests that reward optimization should not be applied equally across all users.

The strongest business opportunity is to reduce rewards for users with low dependency scores while protecting high-dependency users from aggressive cuts.

This creates a more efficient incentive system that improves profitability without blindly damaging retention.
""")