### Project README for GitHub

# Kayak Flight Fare Scraper

This project is a Python-based web scraping automation tool built with Selenium. It scrapes flight fare details from the Kayak website, focusing on the cheapest section. The tool automates the process of clearing filters, selecting Indigo flights, and checking flight details. If the ticket number matches the "to be searched" flight number, it retrieves fare details from all airline provider websites and returns the information to the console. The results can also be exported to Excel using Pandas.

## Features

- Navigate to the Kayak website and select the cheapest section
- Clear all existing filters
- Select Indigo flights
- Check flight details one by one
- Match the ticket number with the "to be searched" flight number
- Retrieve and display fare details from all airline provider websites
- Export fare details to Excel using Pandas

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/KayakScrap.git
    cd kayakscrap
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Update the `config.py` file with the necessary details such as the flight number to be searched.

2. Run the scraper script:

    ```bash
    python scraper.py
    ```

3. The console will display the fare details of the matched flight. If you wish to export the results to an Excel file, make sure to include the relevant code snippet to save the data using Pandas.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to create a pull request or open an issue.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

Thank you for reading and considering contributing to this project. Together, we can make it even better!

---
