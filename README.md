# Reward Dependency Intelligence System

**AI-Powered Incentive Optimization for Rewarded User Acquisition Platforms**

---

## Overview

Rewarded user acquisition platforms invest millions in incentives to drive engagement, retention, and advertiser conversions — yet most apply incentives using static, one-size-fits-all rules. The result: overspending on users who would have stayed engaged regardless of reward level.

This project addresses a high-stakes business question:

> *How much incentive spend can be reduced without negatively impacting user retention or advertiser value?*

The **Reward Dependency Intelligence System** combines behavioral segmentation, dependency scoring, and simulation-based optimization to identify which users genuinely require incentives — and which do not.

---

## Business Problem

Broad reward structures routinely produce:

- Excessive incentive spend with diminishing returns
- Inflated retention metrics that mask true user value
- Poor advertiser ROI due to low-quality, reward-driven engagement
- Limited visibility into user motivation and behavioral patterns

The core challenge is distinguishing users whose engagement is intrinsic from those who are solely driven by reward mechanics.

---

## Solution

The system delivers user-level intelligence across three dimensions:

| Dimension | Output |
|---|---|
| Behavioral Segmentation | Genuine Gamers · Casual Users · Reward Hunters |
| Reward Dependency Scoring | 0 (intrinsically engaged) → 100 (fully reward-dependent) |
| Incentive Optimization | Per-user recommendation: Keep · Reduce 20% · Reduce 40% |

---

## Results

Analysis across **100,000 simulated users** in a multi-country rewarded UA environment:

| Metric | Value |
|---|---|
| Total Users Analysed | 100,000 |
| Current Reward Spend | €1,114,378 |
| Optimized Reward Spend | €957,818 |
| **Estimated Savings** | **€156,561** |
| **Savings Percentage** | **14.05%** |
| High Dependency Users | 24,405 |

### Optimization Breakdown

| Recommendation | Users |
|---|---|
| Reduce Reward by 40% | 39,645 |
| Reduce Reward by 20% | 35,132 |
| Keep Current Reward | 25,223 |

---

## Methodology

### Phase 1 — Behavioral Segmentation

Users are classified into three behavioral archetypes based on engagement patterns, session data, and reward interaction signals:

- **Genuine Gamers** — intrinsically motivated; low reward dependency
- **Casual Users** — moderate engagement; partially incentive-driven
- **Reward Hunters** — engagement tied directly to reward availability

### Phase 2 — Reward Dependency Scoring

Each user receives a continuous dependency score (0–100) derived from behavioral features including session frequency, reward redemption patterns, churn risk, and engagement consistency.

### Phase 3 — Incentive Optimization

Reward reduction scenarios are simulated per user segment, estimating the downstream impact on:

- Retention rate
- Revenue contribution
- Advertiser conversion value
- Incentive efficiency ratio

---

## Dashboard

An interactive Streamlit dashboard provides:

- **Executive KPI summary** — spend, savings, dependency distribution
- **Reward spend analysis** — current vs. optimized, by segment and source
- **Dependency score histogram** — population-level view of incentive reliance
- **Savings breakdown** — by acquisition source and country
- **User-level recommendations** — filterable by country, device, acquisition source, and segment

---

## Tech Stack

| Layer | Tools |
|---|---|
| Data Processing | Python · Pandas · NumPy |
| Modelling | Scikit-Learn |
| Visualization | Plotly · Streamlit |
| Version Control | Git · GitHub |

---

## Future Roadmap

- **Uplift Modelling** — estimate individual treatment effects of reward changes
- **Causal Inference Framework** — move from correlation to causal attribution
- **Reinforcement Learning** — dynamic, real-time reward allocation
- **Advertiser-Specific Strategies** — reward optimization aligned to campaign KPIs
- **Automated Experiment Generation** — continuous A/B testing pipeline

---

## Key Takeaway

Static incentive structures leave significant margin on the table. By scoring reward dependency at the user level, this system enables platforms to reduce incentive spend by **14%+** while preserving retention among users who genuinely need it — turning a blunt cost into a precision instrument.

---

## Author

**Sourav Gupta**  
Data Science · AI · Business Analytics · Product Thinking

[LinkedIn](https://www.linkedin.com/in/sourav-gupta-7539a9217/) · [GitHub](https://github.com/souravgupta166)
