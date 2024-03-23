# Converting CFDI to PDF

## redocmx

The `redocmx` module is a Python client for interacting with the [redoc.mx](https://redoc.mx) REST API to convert CFDIs (Comprobante Fiscal Digital por Internet) to PDFs. 

This client simplifies the process of sending XML data and retrieving the converted PDF, along with transaction details and metadata. 

This package is synchronous.

## Installation

To install the module, run:

```bash
pip install redocmx
```

## Usage

First, import the module and create an instance of the Redoc client. 

You can optionally pass your API key as an argument, or the client will attempt to load it from the REDOC_API_KEY environment variable.

```python
from redocmx import RedocmxClient

redoc =  RedocmxClient('your_api_key_here')
```

### Converting CFDI to PDF

The `redocmx` provides two options for loading CFDI data: from a file or directly from a string.

#### Option 1: Load XML from the File System

```python
cfdi = redoc.cfdi.from_file('./path/to/your/file.xml')
```

#### Option 2: Use an XML Content String

```python
cfdi = redoc.cfdi.from_string('<xml_content_string_here>');
```

### Generating the PDF

To convert the loaded CFDI to a PDF:

```python
try:
	pdf = cfdi.to_pdf()
	
	with open('./nomina.pdf', 'wb') as pdf_file:
		pdf_file.write(pdf.to_buffer())

	print(f"Transaction ID: {pdf.get_transaction_id()}")
	print(f"Total Pages: {pdf.get_total_pages()}")
	print(f"Total Time: {pdf.get_total_time_ms()} ms")
	print(f"Metadata: {pdf.get_metadata()}")
		
except:
	print("An error occurred during the conversion")
```

## Examples

- [Basic example](https://github.com/redocmx/cfdi-a-pdf-ejemplos)
- [Custom logo and colors](https://github.com/redocmx/cfdi-a-pdf-ejemplos)
- [Change language to English](https://github.com/redocmx/cfdi-a-pdf-ejemplos)
- [Add additional rich content](https://github.com/redocmx/cfdi-a-pdf-ejemplos)

## API Reference

### Redoc

The `redoc` object is an instance of `Redoc`, created using `RedocmxClient(api_key)`.

| Method     | Description |
| -------- | ------- |
| redoc.cfdi.**from_file(file_path)**  |  Returns: **Cfdi** - **Instance**<br>Loads file content from the file system for converting a CFDI to PDF. The file should be valid XML for a CFDI.<br>It returns an instance of the Cfdi class, which can be used to obtain the PDF.|
| redoc.cfdi.**from_string(file_content)**  |  Returns: **Cfdi** - **Instance**<br>Uses a CFDI as a string for converting the CFDI to PDF. The string should be valid XML for a CFDI.<br>It returns an instance of the Cfdi class, which can be used to obtain the PDF.|

### Cfdi

The `cfdi` object is an instance of `Cfdi`, created using `redoc.cfdi.from_file(file_path)` or `redoc.cfdi.from_string(file_content)`.

| Method     | Description |
| -------- | ------- |
| cfdi.**set_addenda(str)**  |  Params: **String**<br>Allows the use of a [redoc addenda](https://redoc.mx/docs/addenda) for full control over the design of the final PDF.|
| cfdi.**to_pdf(options)**  |  Params: **Dictionary** - [PdfOptions](#pdfoptions)<br>Returns: **Pdf** - **Instance**<br>An instance of the Pdf class, which, when invoked, converts the CFDI into a PDF and stores it, along with the generated data from the conversion request.|

##### PdfOptions
```python
{
    "style_pdf": "John"
}
```
### Pdf

The `pdf` object is an instance of `Pdf`, created from `cfdi.to_pdf(options)`.

| Method     | Description |
| -------- | ------- |
| pdf.**to_buffer()**  |  Returns: **Buffer**<br>The PDF document as a buffer, ready for storage in the file system or to be sent back in an HTTP request.|
| pdf.**get_transaction_id()**  |  Returns: **String - UUID**<br>A unique ID for the transaction request to the redoc service.|
| pdf.**get_total_pages()** | Returns: **Integer**<br>The total number of pages generated for the PDF file. |
| pdf.**get_total_time_ms()**    | Returns: **Integer**<br>Time in milliseconds taken to convert the CFDI to PDF. |
| pdf.**get_metadata()**    | Returns: **Dictionary** - [CfdiMetadata]()<br>General information from the converted CFDI. |

##### CfdiMetadata
```js 
{
    TDB...
}
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs, features, or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.