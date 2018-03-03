amazonproducts_extract_html_to_xml.py: For amazon products, it takes the HTMl and extracts the products for each page and converts it into XML for analysis. This one is catered for books but can easily be changed for other kinds of products.

Run: python extract.py results1.html results1.xml

tsv_to_xml.py: Converts a tsv file into xml for xpath analysis

Run: python tsv_to_xml.py parks.tsv parks.xml

xml_stats.py: Quick show of extracting simple statistics from xml. 

Run: python xml_stats.py parks.xml
