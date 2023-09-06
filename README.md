# GENESIS Data Scraper

![GENESIS Data Scraper](https://your_image_url_here.com)

This project provides a convenient way to scrape data from GENESIS-Online by simply entering your GENESIS username, password, and the table name(s) you wish to extract. The scraped data is then saved as CSV files, with each file named after its respective table.

## Getting Started

Follow these steps to set up and run the GENESIS Data Scraper on your local machine:

### Prerequisites

Before getting started, ensure you have Python and pip installed on your system.

### Installation

1. Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/milanbeherazyx/GENESIS_DataMiner.git
   ```

2. Navigate to the project directory:

   ```bash
   cd GENESIS_DataMiner
   ```

3. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the Streamlit app with the following command:

   ```bash
   streamlit run app.py
   ```

2. Access the Streamlit app in your web browser at [http://localhost:8501](http://localhost:8501).

3. Follow these steps within the Streamlit app:
   - Enter your GENESIS username and password.
   - Input the table name(s) you want to scrape (comma-separated).
   - Click the "Enter" button to initiate the scraping process.

### Saving Data

The scraped data will be saved in the project directory. Each CSV file will be named after its corresponding table.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

Special thanks to the GENESIS-Online community for inspiration and support.

Feel free to contribute and improve this project. Happy data scraping!