
# LLaMA-Test

## Setup Instructions

1. **Clone the Repository**
   - First, clone the repository to your local machine:
     ```bash
     git clone <repository-url>
     ```

2. **Install Dependencies**
   - After cloning the repository, navigate to the project directory and install the required dependencies by running:
     ```bash
     pip install streamlit
     ```

## Updating the API URL

1. **Start the Virtual Machine**
   - Start your virtual machine (VM).

2. **Copy the External API URL**
   - Once the VM is running, obtain the external IP address.

3. **Update `app.py`**
   - Open `app.py` and locate the `api_url` variable.
   - Replace the placeholder IP `34.46.213.152` with your newly generated external IP address.

## Running the Application

- To run the Streamlit application, execute the following command in your terminal:
  ```bash
  streamlit run app.py
