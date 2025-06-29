# import os
# import subprocess
# import sys
# import streamlit as st
# from typing import List

# # ===== DEPENDENCY INSTALLATION =====
# def install_dependencies(requirements: List[str] = None):
#     """Install required dependencies if missing"""
#     if requirements is None:
#         requirements = [
#             'joblib>=1.2.0',
#             'pandas>=1.5.0',
#             'scikit-learn>=1.0.0',
#             'streamlit>=1.0.0'
#         ]
    
#     try:
#         import importlib
#         for package in requirements:
#             pkg_name = package.split('>')[0].split('<')[0].split('=')[0]
#             importlib.import_module(pkg_name)
#     except ImportError:
#         st.warning("Installing missing dependencies...")
#         try:
#             subprocess.check_call([
#                 sys.executable,
#                 "-m",
#                 "pip",
#                 "install",
#                 *requirements
#             ])
#             st.success("Dependencies installed successfully! Please refresh the page.")
#             st.stop()  # Stop execution to allow refresh
#         except subprocess.CalledProcessError as e:
#             st.error(f"Failed to install dependencies: {e}")
#             st.stop()
            

# # Install dependencies at startup


# # ===== MAIN APP =====
# def main():
#     st.set_page_config(
#         page_title="Telecom Churn Prediction",
#         page_icon="📊",
#         layout="wide"
#     )
    
#     st.title("📱 Telecom Customer Churn Prediction")
#     st.markdown("""
#     This app predicts customer churn probability based on telecom usage patterns.
#     Upload your customer data below to get predictions.
#     """)
    
#     # Sidebar for settings/options
#     with st.sidebar:
#         st.header("Settings")
#         confidence_threshold = st.slider(
#             "Churn probability threshold",
#             min_value=0.5,
#             max_value=1.0,
#             value=0.7,
#             step=0.05,
#             help="Adjust the confidence level for churn classification"
#         )
    
#     # Main content area
#     tab1, tab2 = st.tabs(["Data Upload", "Batch Prediction"])
    
#     with tab1:
#         st.subheader("Upload Customer Data")
#         uploaded_file = st.file_uploader(
#             "Choose a CSV file",
#             type=["csv"],
#             accept_multiple_files=False,
#             help="Upload your customer data in CSV format"
#         )
        
#         if uploaded_file is not None:
#             try:
#                 import pandas as pd
#                 df = pd.read_csv(uploaded_file)
                
#                 st.success("File uploaded successfully!")
#                 st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
                
#                 if st.checkbox("Show data preview"):
#                     st.dataframe(df.head())
                
#                 # Add your prediction logic here
#                 if st.button("Predict Churn"):
#                     with st.spinner("Making predictions..."):
#                         # Replace with your actual prediction code
#                         # Example placeholder:
#                         predictions = [0.65, 0.82, 0.43]  # Example probabilities
#                         df['Churn Probability'] = predictions
#                         df['Churn Prediction'] = df['Churn Probability'].apply(
#                             lambda x: 'Yes' if x >= confidence_threshold else 'No'
#                         )
                        
#                         st.success("Predictions complete!")
#                         st.dataframe(df)
                        
#                         # Download button
#                         csv = df.to_csv(index=False).encode('utf-8')
#                         st.download_button(
#                             label="Download predictions",
#                             data=csv,
#                             file_name="churn_predictions.csv",
#                             mime="text/csv"
#                         )
                        
#             except Exception as e:
#                 st.error(f"Error processing file: {str(e)}")
    
#     with tab2:
#         st.subheader("Batch Prediction")
#         st.info("Coming soon! This feature will allow processing multiple files at once.")

# # ===== RUN THE APP =====
# if __name__ == "__main__":
#     try:
#         main()
#     except ImportError as e:
#         st.error(f"Missing dependency: {e}")
#         if st.button("Install dependencies"):
#             install_dependencies()
#             st.experimental_rerun()

import os
import streamlit as st
from typing import List

def check_dependencies() -> bool:
    """Check if all required packages are installed"""
    required_packages = [
        'pandas',
        'scikit-learn',
        'joblib',
        'streamlit',
        'markdown-it-py',
        'Pygments'
    ]
    
    try:
        import importlib
        for package in required_packages:
            importlib.import_module(package)
        return True
    except ImportError:
        return False

def main():
    """Main application logic"""
    st.set_page_config(
        page_title="Telecom Churn Prediction",
        page_icon="📊",
        layout="wide"
    )
    
    st.title("📱 Telecom Customer Churn Prediction")
    st.markdown("Upload customer data to predict churn probability")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    if uploaded_file:
        try:
            import pandas as pd
            df = pd.read_csv(uploaded_file)
            st.success("File uploaded successfully!")
            st.write(f"Rows: {len(df)}, Columns: {len(df.columns)}")
            
            if st.checkbox("Show data preview"):
                st.dataframe(df.head())
                
            if st.button("Predict Churn"):
                with st.spinner("Making predictions..."):
                    # Replace with actual prediction logic
                    predictions = [0.65, 0.82, 0.43] * len(df)  # Example
                    df['Churn Probability'] = predictions[:len(df)]
                    df['Churn Prediction'] = df['Churn Probability'].apply(
                        lambda x: 'Yes' if x >= 0.7 else 'No'  # Default threshold
                    )
                    
                    st.success("Predictions complete!")
                    st.dataframe(df)
                    
                    # Download button
                    csv = df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="Download predictions",
                        data=csv,
                        file_name="churn_predictions.csv",
                        mime="text/csv"
                    )
                    
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")

if __name__ == "__main__":
    if not check_dependencies():
        st.warning("Setting up environment...")
        try:
            import subprocess
            import sys
            subprocess.check_call([sys.executable, "setup.py"])
            st.success("Dependencies installed! Please refresh your browser.")
            st.stop()
        except Exception as e:
            st.error(f"Setup failed: {str(e)}")
            st.stop()
    else:
        main()