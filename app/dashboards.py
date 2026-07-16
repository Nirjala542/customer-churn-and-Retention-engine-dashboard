import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="Customer Churn Dashboard",
    page_icon="📊",
    layout="wide"
)

# Inject custom CSS for premium styling, backgrounds, and hover effects
st.markdown("""
<style>
/* Style the main background with a premium radial gradient glow */
div[data-testid="stAppViewContainer"] {
    background-color: #0b0f19 !important;
    background-image: 
        radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.12) 0px, transparent 50%),
        radial-gradient(at 50% 0%, rgba(59, 130, 246, 0.08) 0px, transparent 50%),
        radial-gradient(at 100% 0%, rgba(147, 51, 234, 0.12) 0px, transparent 50%),
        radial-gradient(at 50% 100%, rgba(30, 41, 59, 0.4) 0px, transparent 50%) !important;
    background-attachment: fixed !important;
}

/* Style the top header as transparent */
header[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0) !important;
}

/* Style the sidebar with a glassmorphic look */
section[data-testid="stSidebar"] {
    background-color: rgba(15, 23, 42, 0.7) !important;
    backdrop-filter: blur(15px) !important;
    -webkit-backdrop-filter: blur(15px) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
}

/* Style metric containers as modern cards */
div[data-testid="stMetric"] {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.8) 100%);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 20px 24px !important;
    border-radius: 16px !important;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -4px rgba(0, 0, 0, 0.3);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

/* Hover Effect for metric cards */
div[data-testid="stMetric"]:hover {
    transform: translateY(-5px) scale(1.02);
    border-color: rgba(99, 102, 241, 0.6);
    box-shadow: 0 20px 25px -5px rgba(99, 102, 241, 0.3), 0 8px 10px -6px rgba(99, 102, 241, 0.3);
}

/* Subtle glowing accent line on hover */
div[data-testid="stMetric"]::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg, #6366f1, #3b82f6);
    opacity: 0;
    transition: opacity 0.3s ease;
}

div[data-testid="stMetric"]:hover::before {
    opacity: 1;
}

/* Style metric labels */
div[data-testid="stMetric"] label {
    font-size: 0.9rem !important;
    font-weight: 600 !important;
    color: #94a3b8 !important;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

/* Style metric values */
div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
    font-size: 2.2rem !important;
    font-weight: 700 !important;
    color: #f8fafc !important;
    margin-top: 8px;
}

/* Style the delta indicator */
div[data-testid="stMetric"] div[data-testid="stMetricDelta"] {
    font-weight: 600 !important;
}

/* Also style custom info/success/warning cards with smooth hover transition */
div[data-testid="stAlert"] {
    border-radius: 12px !important;
    transition: all 0.3s ease-in-out;
}
div[data-testid="stAlert"]:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
}

/* Style the sidebar option menu card-like feel */
.nav-link {
    transition: all 0.2s ease-in-out !important;
}
.nav-link:hover {
    background-color: rgba(99, 102, 241, 0.15) !important;
    transform: translateX(4px);
}
</style>
""", unsafe_allow_html=True)

df = pd.read_csv("telco_cleaned.csv")
# page = st.sidebar.radio(
    
#     "Go to",
#     [
#         "🏠 Dashboard",
#         "📊 EDA",
#         "📈 Analytics",
#         "👥 Customer Profile",
#         "⚠️ High Risk Customers",
#         "💰 Revenue Analysis",
#         "🎯 Retention Engine",
#         "📉 Churn Prediction",
#         "📋 Business Insights",
#         "ℹ️ About"
#     ]
# )
with st.sidebar:
    page=option_menu("Menu",options=[
        " Dashboard",
        " EDA",
        " Analytics",
        " Customer Profile",
        " High Risk Persons",
        " Revenue Analysis",
        " Retention Engine",
       
        " Business Insights",
        " About"],
            icons=[
                "house-fill",
                "bar-chart-fill",
                "graph-up",
                "person-fill",
                "exclamation-triangle-fill",
                "cash-stack",
                "bullseye",
                
                "clipboard-data-fill",
                "info-circle-fill"
                ],default_index=0)
if page == " Dashboard":
    st.title("(❁´◡`❁) Customer Churn and Retention Dashboard")
    total_customers = len(df)
    total_churn = df[df["Churn Label"] == "Yes"].shape[0]
    total_revenue = df["Total Revenue"].sum()
    avg_cltv = df["CLTV"].mean()
    # Customer Lifetime Value.
    avg_monthly = df["Monthly Charge"].mean()
    st.markdown("---")
    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("👥 Customers", f"{total_customers:,}")
    c2.metric("❌ Churn", total_churn)
    c3.metric("💰 Revenue", f"${total_revenue:,.0f}")
    c4.metric("⭐ Avg CLTV", f"{avg_cltv:.0f}")
    c5.metric("📈 Avg Monthly", f"${avg_monthly:.2f}")

    st.markdown("---")
    fig = px.scatter(
            df,
            x="Tenure in Months",
            y="Total Revenue",
            color="Churn Label",
            title="Tenure vs Total Revenue",
            color_discrete_map={
                "No": "#5B8FF9",
                "Yes": "#F97316"
            }
        )
    
    fig.update_layout(
            title_x=0.5,
            height=300,
            margin=dict(l=10, r=10, t=40, b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )
    
    st.plotly_chart(fig, use_container_width=True)
    fig1 = px.pie(
        df,
        names="Churn Label",
        hole=0.68,
        title="Customer Churn Distribution",
        color="Churn Label",
        color_discrete_map={
            "No": "#5B8FF9",      # Premium Blue
            "Yes": "#F97316"      # Vibrant Orange
        }
    )

    fig1.update_traces(
        textinfo="percent+label",
        textfont_size=15,
        marker=dict(
            line=dict(color="#1F2937", width=2)
        )
    )

    fig1.update_layout(
        title=dict(
            text="Customer Churn Distribution",
            x=0.5,
            font=dict(size=20)
        ),
        font=dict(size=13, color="#E5E7EB"),
        paper_bgcolor="rgba(0,0,0,0)",  
        plot_bgcolor="rgba(0,0,0,0)",    
        legend=dict(
            orientation="h",
            y=-0.15,
            x=0.25,
            font=dict(size=12)
        ),
        margin=dict(l=10, r=10, t=60, b=10)
    )
    contract = df["Contract"].value_counts().reset_index()
    contract.columns = ["Contract", "Customers"]

    fig2 = px.bar(
        contract,
        x="Contract",
        y="Customers",
        color="Contract",
        text_auto=True,
        title="Customers by Contract"
        
    )

    fig3 = px.box(
    df,
    x="Churn Label",
    y="Monthly Charge",
    color="Churn Label",
    title="Monthly Charges by Customer Status",
    color_discrete_map={
        "No": "#5B8FF9",
        "Yes": "#F97316"
    }
)
    
    col1, col2,blank = st.columns([1,1,0.85])
    with blank:
        
           
        churn_rate = (df["Churn Label"] == "Yes").mean() * 100

        if churn_rate > 25:
                    st.error(f"""
            🚨 **High Churn Alert**

            Current Churn Rate: **{churn_rate:.1f}%**

            Immediate customer retention actions are recommended.
            """)
        else:
                    st.success("✅ Customer churn is under control.")
        st.subheader("🏆 Top Revenue Customers")
            
        top = df.nlargest(3, "Total Revenue")[["Customer ID", "Total Revenue"]]
            
        st.dataframe(top, hide_index=True, use_container_width=True)
                    
    with col1:
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.plotly_chart(fig2, use_container_width=True)



    col3, blank = st.columns([1,1])

    with col3:
        st.plotly_chart(fig3, use_container_width=True)
    with blank:
        with blank:

            st.subheader("🚨 Top 10 High Risk Customers")

            top10 = (
                df.nlargest(10, "Churn Score")
                [["Customer ID", "Churn Score", "Customer Status"]]
            )

            st.dataframe(top10, hide_index=True, use_container_width=True)
    fig = px.scatter_map(
    df,
            lat="Latitude",
            lon="Longitude",
            color="Churn Label",
            hover_name="Customer ID",
            hover_data=["City", "State", "Monthly Charge"],
            zoom=3,
            height=350,
            color_discrete_map={
                "No": "#5B8FF9",
                "Yes": "#F97316"
            }
        )    

    st.plotly_chart(fig, use_container_width=True)
elif page == " EDA":
    st.title("📊 Exploratory Data Analysis")
    total_customers = len(df)
    total_churn = df[df["Churn Label"] == "Yes"].shape[0]
    total_revenue = df["Total Revenue"].sum()
    avg_cltv = df["CLTV"].mean()
    # Customer Lifetime Value.
    avg_monthly = df["Monthly Charge"].mean()
    st.markdown("---")
    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("👥 Customers", f"{total_customers:,}")
    c2.metric("❌ Churn", total_churn)
    c3.metric("💰 Revenue", f"${total_revenue:,.0f}")
    c4.metric("⭐ Avg CLTV", f"{avg_cltv:.0f}")
    c5.metric("📈 Avg Monthly", f"${avg_monthly:.2f}")

    st.markdown("---")
    st.subheader("dataset preview")
    df = pd.read_csv("telco_cleaned.csv")
    dataframe=df.head(8)
    st.dataframe(dataframe)
    st.markdown("---")
    st.subheader("dataset shape")
    c1,c2=st.columns(2)
    with c1:
        st.metric("Rows",df.shape[0])
    with c2:
        st.metric("Columns",df.shape[1])
    st.markdown("---")
    st.subheader("dataset Describe")
    st.dataframe(df.describe().T)
    st.markdown("---")
    st.subheader("ℹ️ Dataset Information")

    info = pd.DataFrame({
        "Column Name": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Non-Null Count": df.count().values
    })
    st.dataframe(info, use_container_width=True)
    st.subheader("❗ Missing Values")

    missing = df.isnull().sum().reset_index()
    missing.columns = ["Column", "Missing Values"]

    st.dataframe(missing[missing["Missing Values"] > 0], use_container_width=True)
    st.subheader("🔁 Duplicate Values")

    duplicates = df.duplicated().sum()

    st.metric("Total Duplicate Rows", duplicates)



elif page == " Analytics":
    st.title("📈 Customer Analytics")
    st.divider()
    total_customers = len(df)
    churn_customers = df[df["Churn Label"]=="Yes"].shape[0]
    retained_customers = df[df["Churn Label"]=="No"].shape[0]
    total_revenue = df["Total Revenue"].sum()

    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.metric("👥 Total Customers", f"{total_customers:,}")

    with k2:
        st.metric("❌ Churn Customers", f"{churn_customers:,}")

    with k3:
        st.metric("✅ Retained Customers", f"{retained_customers:,}")

    with k4:
        st.metric("💰 Total Revenue", f"${total_revenue:,.0f}")
    st.divider()
    col1, col2, col3, col4 = st.columns(4)
    with col1:

        fig6= px.pie(
            df,
            names="Churn Label",
            hole=0.65,
            color="Churn Label",
            color_discrete_sequence=["#00CC96", "#EF553B"]
        )

        fig6.update_layout(
            title="Churn Distribution",
            height=280,
            margin=dict(l=10,r=10,t=40,b=10),
            showlegend=True
        )

        st.plotly_chart(fig6, use_container_width=True)
    with col2:

        status = df["Customer Status"].value_counts().reset_index()
        status.columns = ["Customer Status","Count"]

        fig7 = px.bar(
            status,
            x="Customer Status",
            y="Count",
            color="Customer Status",
            text_auto=True
        )

        fig7.update_layout(
            title="Customer Status",
            height=280,
            margin=dict(l=10,r=10,t=40,b=10),
            showlegend=True
        )

        st.plotly_chart(fig7, use_container_width=True)
    with col3:

        fig8 = px.treemap(
            df,
            path=["Contract"],
            color="Contract"
        )

        fig8.update_layout(
            title="Contract Type",
            height=280,
            margin=dict(l=5,r=5,t=40,b=5)
        )

        st.plotly_chart(fig8, use_container_width=True)
        with col4:
            fig9 = px.histogram(
                df,
                x="Monthly Charge",
                nbins=25,
                color="Customer Status",
                color_discrete_map={
                    "Stayed": "#5B8FF9",
                    "Churned": "#F97316",
                    "Joined": "#10B981"
                }
            )

            fig9.update_layout(
                title="Monthly Charges",
                title_x=0.5,
                height=280,
                margin=dict(l=10, r=10, t=40, b=10)
            )

            st.plotly_chart(fig9, use_container_width=True)
        
    col7, col8 = st.columns(2)

    with col7:

        fig12 = px.box(
            df,
            y="Tenure in Months",
            color="Churn Label",
            title="Tenure Analysis",
            color_discrete_sequence=["#00CC96", "#EF553B"]
        )

        fig12.update_layout(
            height=300,
            margin=dict(l=5, r=5, t=45, b=5),
            showlegend=True
        )

        st.plotly_chart(fig12, use_container_width=True)


    with col8:

        payment = (
            df["Payment Method"]
            .value_counts()
            .reset_index()
        )
        payment.columns = ["Payment Method", "Count"]

        fig13 = px.bar(
            payment,
            x="Count",
            y="Payment Method",
            orientation="h",
            text_auto=True,
            color="Payment Method",
            title="Payment Method"
        )

        fig13.update_layout(
            height=300,
            margin=dict(l=5, r=5, t=45, b=5),
            showlegend=False
        )

        st.plotly_chart(fig13, use_container_width=True)
    internet = (
    df.groupby(["Internet Service", "Churn Label"])
    .size()
    .reset_index(name="Count")
)

    fig11 = px.bar(
        internet,
        x="Internet Service",
        y="Count",
        color="Churn Label",
        barmode="stack",
        text_auto=True,
        title="Internet Service vs Churn",
        color_discrete_map={
            "No": "#5B8FF9",
            "Yes": "#F97316"
        }
    )

    fig11.update_layout(
        title_x=0.5,
        height=300,
        margin=dict(l=10, r=10, t=40, b=10)
    )

    st.plotly_chart(fig11, use_container_width=True)
elif page == " Customer Profile":
    st.title("👥 Customer Profile")
    customer_id = st.selectbox(
        "Select Customer ID",
        df["Customer ID"].unique()
    )
    customer = df[df["Customer ID"] == customer_id].iloc[0]

    st.divider()
    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.metric("👤 Customer ID", customer["Customer ID"])

    with k2:
        st.metric("📅 Tenure", f'{customer["Tenure in Months"]} Months')

    with k3:
        st.metric("💰 Monthly Charge", f'${customer["Monthly Charge"]:.2f}')

    with k4:
        st.metric("⭐ Churn Score", customer["Churn Score"])

    st.divider()

    left, right = st.columns(2)

    with left:
        st.subheader("👤 Personal Details")

        st.write("**Gender:**", customer["Gender"])
        st.write("**Age:**", customer["Age"])
        st.write("**Senior Citizen:**", customer["Senior Citizen"])
        st.write("**Married:**", customer["Married"])
        st.write("**Dependents:**", customer["Number of Dependents"])

    with right:
        st.subheader("📄 Account Details")

        st.write("**Contract:**", customer["Contract"])
        st.write("**Internet Service:**", customer["Internet Service"])
        st.write("**Payment Method:**", customer["Payment Method"])
        st.write("**Customer Status:**", customer["Customer Status"])
        st.write("**Churn Label:**", customer["Churn Label"])

    st.divider()


    if customer["Churn Label"] == "Yes":
        st.error("🔴 High Churn Risk Customer")
    else:
        st.success("🟢 Low Churn Risk Customer")

    st.divider()
    st.subheader("🎯 Retention Recommendation")

    if customer["Churn Label"] == "Yes":

        st.info("""
    ✅ Offer loyalty discount

    ✅ Provide free Tech Support

    ✅ Recommend yearly contract

    ✅ Follow-up customer call
    """)

    else:

        st.success("""
    Customer is loyal.

    Continue providing quality service and reward with loyalty offers.
    """)

elif page == " High Risk Persons":
    st.title("⚠️ High Risk Customers")

    high_risk = (
            df[df["Churn Score"] >= 80]
            .sort_values(by="Churn Score", ascending=False)
        )

    k1, k2, k3, k4 = st.columns(4)

    with k1:
            st.metric("🔴 High Risk Customers", len(high_risk))

    with k2:
            st.metric(
                "⭐ Avg Churn Score",
                round(high_risk["Churn Score"].mean(), 1)
            )

    with k3:
            st.metric(
                "💰 Revenue at Risk",
                f"${high_risk['Total Revenue'].sum():,.0f}"
            )

    with k4:
            st.metric(
                "💳 Avg Monthly Charge",
                f"${high_risk['Monthly Charge'].mean():.2f}"
            )

    st.divider()

    contract = st.selectbox(
            "Contract Type",
            ["All"] + list(df["Contract"].unique())
        )

    if contract != "All":
            high_risk = high_risk[high_risk["Contract"] == contract]

    st.subheader("📋 High Risk Customer List")

    st.dataframe(
            high_risk[
                [
                    "Customer ID",
                    "Gender",
                    "Age",
                    "Tenure in Months",
                    "Monthly Charge",
                    "Contract",
                    "Payment Method",
                    "Customer Status",
                    "Churn Score",
                    "Churn Label"
                ]
            ],
            use_container_width=True,
            hide_index=True
        )

    csv = high_risk.to_csv(index=False).encode("utf-8")

    st.download_button(
            "⬇️ Download High Risk Customers",
            data=csv,
            file_name="High_Risk_Customers.csv",
            mime="text/csv"
        )

elif page == " Revenue Analysis":
        st.title("💰 Revenue Analysis")
        total_revenue = df["Total Revenue"].sum()
        avg_revenue = df["Total Revenue"].mean()
        avg_monthly = df["Monthly Charge"].mean()
        avg_cltv = df["CLTV"].mean()

        k1, k2, k3, k4 = st.columns(4)

        with k1:
            st.metric("💰 Total Revenue", f"${total_revenue:,.0f}")

        with k2:
            st.metric("📈 Avg Revenue", f"${avg_revenue:,.2f}")

        with k3:
            st.metric("💳 Avg Monthly Charge", f"${avg_monthly:,.2f}")

        with k4:
            st.metric("⭐ Avg CLTV", f"${avg_cltv:,.0f}")

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            revenue_status = (
                df.groupby("Customer Status")["Total Revenue"]
                .sum()
                .reset_index()
            )

            fig1 = px.bar(
                revenue_status,
                x="Customer Status",
                y="Total Revenue",
                color="Customer Status",
                text_auto=".2s",
                title="Revenue by Customer Status"
            )

            st.plotly_chart(fig1, use_container_width=True)

        with col2:

            fig2 = px.histogram(
                df,
                x="Monthly Charge",
                nbins=30,
                title="Monthly Charge Distribution",
                color_discrete_sequence=["#636EFA"]
            )

            st.plotly_chart(fig2, use_container_width=True)

        col3, col4 = st.columns(2)

        with col3:

            contract_revenue = (
                df.groupby("Contract")["Total Revenue"]
                .sum()
                .reset_index()
            )

            fig3 = px.pie(
                contract_revenue,
                names="Contract",
                values="Total Revenue",
                hole=0.6,
                title="Revenue by Contract"
            )

            st.plotly_chart(fig3, use_container_width=True)

        with col4:

            fig4 = px.box(
                df,
                x="Churn Label",
                y="Total Revenue",
                color="Churn Label",
                title="Revenue vs Churn"
            )

        st.plotly_chart(fig4, use_container_width=True)

elif page == " Retention Engine":
    st.title("🎯 Retention Engine")

    customer_id = st.selectbox(
        "Select Customer ID",
        df["Customer ID"].unique()
    )

    customer = df[df["Customer ID"] == customer_id].iloc[0]

    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.metric("⭐ Churn Score", customer["Churn Score"])

    with k2:
        st.metric("💰 Monthly Charge", f"${customer['Monthly Charge']:.2f}")

    with k3:
        st.metric("📅 Tenure", f"{customer['Tenure in Months']} Months")

    with k4:
        st.metric("📄 Contract", customer["Contract"])

    st.divider()

    st.subheader("📋 Customer Details")

    c1, c2 = st.columns(2)

    with c1:
        st.write("**Customer Status:**", customer["Customer Status"])
        st.write("**Internet Service:**", customer["Internet Service"])
        st.write("**Payment Method:**", customer["Payment Method"])

    with c2:
        st.write("**Contract:**", customer["Contract"])
        st.write("**Premium Tech Support:**", customer["Premium Tech Support"])
        st.write("**Online Security:**", customer["Online Security"])

    st.divider()

    st.subheader(" Retention Recommendation")

    if customer["Churn Score"] >= 80:
        st.error("""
    🔴 High Risk Customer

    **Recommended Actions**
    - Offer 20% loyalty discount
    - Upgrade to yearly contract
    - Provide free Tech Support
    - Priority customer support
    """)

    elif customer["Churn Score"] >= 50:
        st.warning("""
    🟡 Medium Risk Customer

    **Recommended Actions**
    - Send promotional offers
    - Recommend bundled services
    - Follow-up with customer
    """)

    else:
        st.success("""
    🟢 Low Risk Customer

    **Recommended Actions**
    - Reward with loyalty points
    - Continue regular engagement
    - Recommend premium plans
    """)

elif page == " Business Insights":
    st.title("📋 Business Insights")
    st.info("""
    The customer churn analysis reveals that contract type, monthly charges,
    customer tenure, and support-related services are the major factors influencing customer churn.
    These insights help businesses reduce customer loss, improve retention strategies,
    and maximize long-term revenue.
    """)

    st.divider()
    st.subheader("📈 Business Health Meter")

    revenue_score = min((df["Total Revenue"].sum() / 16000000) * 100, 100)

    retention_score = (df["Churn Label"] == "No").mean() * 100

    satisfaction_score = (df["Satisfaction Score"].mean() / 5) * 100

    risk_score = 100 - ((df["Churn Score"].mean() / 100) * 100)

    st.write("💰 Revenue Health")
    st.progress(revenue_score / 100)
    st.caption(f"{revenue_score:.1f}%")

    st.write("👥 Customer Retention")
    st.progress(retention_score / 100)
    st.caption(f"{retention_score:.1f}%")

    st.write("😊 Customer Satisfaction")
    st.progress(satisfaction_score / 100)
    st.caption(f"{satisfaction_score:.1f}%")

    st.write("🚨 Risk Level")
    st.progress(risk_score / 100)
    st.caption(f"{risk_score:.1f}%")
    st.subheader("📌 Key Business Findings")

    col1, col2 = st.columns(2)

    with col1:
        st.success("""
    ### 📄 Contract Type

    - Month-to-Month customers have the highest churn rate.
    - Long-term contract customers are more loyal.
    - Encouraging yearly contracts can improve retention.
    """)

    with col2:
        st.warning("""
    ### 💰 Monthly Charges

    - Customers with higher monthly charges are more likely to churn.
    - Competitive pricing and attractive offers can reduce churn.
    """)

    col3, col4 = st.columns(2)

    with col3:
        st.info("""
    ### ⏳ Customer Tenure

    - Customers with longer tenure show higher loyalty.
    - New customers require better engagement and onboarding.
    """)

    with col4:
        st.error("""
    ### 🛠 Support Services

    - Customers without Online Security or Tech Support are at higher churn risk.
    - Promoting support services can improve customer satisfaction.
    """)

    st.divider()

    st.subheader("⚠️ Business Risks")

    st.warning("""
    - High dependency on Month-to-Month contracts.
    - Increasing customer acquisition costs.
    - Loss of high-value customers.
    - Reduced long-term revenue.
    - Lower customer satisfaction.
    """)

    st.divider()

    st.subheader("🎯 Recommended Business Actions")

    st.success("""
    - Introduce loyalty rewards for long-term customers.
    - Encourage customers to choose yearly contracts.
    - Offer personalized discounts to high-risk customers.
    - Improve Tech Support and Online Security services.
    - Contact customers before contract renewal.
    - Continuously monitor high-risk customers.
    """)

    st.divider()

    st.subheader("📈 Expected Business Benefits")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Customer Retention", "⬆️ Higher")

    with col2:
        st.metric("Revenue Stability", "⬆️ Improved")

    with col3:
        st.metric("Customer Satisfaction", "⬆️ Better")

    st.divider()

    st.subheader("🚀 Future Scope")

    st.info("""
    - AI-powered retention recommendations.
    - Real-time churn prediction.
    - CRM integration.
    - Automated customer alerts.
    - Personalized marketing campaigns.
    - Customer feedback sentiment analysis.
    """)

elif page == " About":
    st.title("ℹ️ About Project")
    st.subheader("🚀 Dashboard Highlights")
    st.success("✔ Analyze 7,043 customer records in one place.")
    st.success("✔ Interactive charts for quick business understanding.")
    st.success("✔ Identify high-risk customers instantly.")
    st.success("✔ Monitor revenue and customer lifetime value.")
    st.success("✔ Explore data without writing any code.")

    st.title("💡 Did You Know?")

    st.info("""
    Even a small reduction in customer churn can significantly increase
    business revenue and customer lifetime value.

    This dashboard helps businesses identify churn patterns early,
    understand customer behavior, and make smarter retention decisions.
    """)
