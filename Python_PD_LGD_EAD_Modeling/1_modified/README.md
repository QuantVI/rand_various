# Credit Risk Modeling 
###### - Project Syllabus

Using consumer loan data, we design a model to predict the probability
of default. We also assign a default prediction and tune it according to
out-of-sample metrics.

In conjunction with a probability of default (PD) model, we create a
loss given default (LGD) model and and exposure at default (EAD) model.
The three are combined to predict the Expected Credit Loss (ECL).

| Section                                    | Sub-section                              |
| ------------------------------------------ | ---------------------------------------- |
| 01. Introduction                           | 01A.  Purpose                            |
|                                            | 01B.  Scope                              |
|                                            | 01C.  Terminology                        |
|                                            | 01D.  Report Structure                   |
| 02. Dev Environment                        | 02A.  Software & Tools                   |
|                                            | 02B.  Data & Permissions                 |
|                                            | 02C.  Folder Structure                   |
|                                            | 02D.  Git                                |
| 03. Data Definition                        | 03A.  Sources                            |
|                                            | 03B.  Variables                          |
|                                            | 03C.  Size & Timespan                    |
|                                            | 03D.  Initial Quality Assurance          |
| 04. Preprocessing                          | 04A.  Missing Data                       |
|                                            | 04B.  Outliers                           |
|                                            | 04C.  Categorical Variables              |
|                                            | 04D.  Train-test Split                   |
| 05. **PD Model**: Data Preparation         | 05A.  Defining Default                   |
|                                            | 05B.  Feature Engineering                |
|                                            | 05C.  Timing Alignment                   |
|                                            | 05D.  Exclusions                         |
| 06. **PD Model**: Estimation               | 06A.  Algorithm Selection                |
|                                            | 06B.  Model Training                     |
|                                            | 06C.  Hyper-parameter Tuning              |
|                                            | 06D.  Coefficient Interpretation         |
|                                            | 06E.  Cross-validation                   |
|                                            | 06F.  Performance Metrics                |
|                                            | 06G.  Back-testing                       |
|                                            | 06H.  Benchmarking                       |
| 07. **PD Model**: Application               | 07A.  Score Thresholds                   |
|                                            | 07B.  Risk-based Pricing                 |
|                                            | 07C.  Portfolio Risk                     |
|                                            | 07D. Stakeholder Reporting               |
| 08. **PD Model**: Monitoring               | 08A.  Performance Drift                  |
|                                            | 08B.  Model Stability                    |
|                                            | 08C.  Recalibration Triggers             |
|                                            | 08D.  Monitoring Dashboard               |
| 09. **LGD & EAD Models**: Data Preparation | 09A.  LGD Target                         |
|                                            | 09B.  EAD Target                         |
|                                            | 09C.  Data Segmentation                 |
|                                            | 09D.  Confidential Data                  |
| 10. **LGD Model**: Estimation              | 10A.  Model Selection                    |
|                                            | 10B.  Feature Importance                 |
|                                            | 10C.  Model Validation                   |
|                                            | 10D.  Loss Forecasting                   |
|                                            | 10E.  Model Selection                    |
|                                            | 10F.  Feature Engineering                |
|                                            | 10G.  Validation Metrics                 |
| 11. **Expected Loss** Calculation          | 11A.  Combining PD, LGD, EAD             |
|                                            | 11B.  Stress Testing & Scenario Analysis |
|                                            | 11C.  Regulatory Reporting               |
