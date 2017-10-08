# PACInterview
Crawler of Microsoft Academic and Google Scholar implemented with python

## Usage
1. Microsoft Academic Crawler
```
python3 MSSpider.py
```

2. Microsoft Academic API (POST way)
Purpose: pack Q1 function as an API(POST way) in flask framework
Step 1. Run the server
```
python3 MSapi.py
```
Step 2. Send POST request in the folloing format
Example: http://127.0.0.1:8000/msscholar/Fin10K
```
http://127.0.0.1:8000/msscholar/<query>
```  

3. Google Scholar Crawler
Purpose: use python to build a crawler for the following website
(NOTE): The function cannot crawl target page because it will be detect as ROBOT. The program only implemeted the parser part.
```
python3 GoogleScholarSpider.py GoogleSchlar_sample_file.html
```

4. free text mining.txt parser
Purpose: Parse the paper titles form attachment file "free text mining.txt"
```
python3 free_text_parser.py [target_file]
```
Example Usage
```
python3 free_text_parser.py free_text_mining.txt
```

5. Question
Answer shows in file "5_answer.txt"
