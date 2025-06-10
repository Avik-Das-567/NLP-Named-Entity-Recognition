# NLP - Named Entity Recognition (NER)
### Open in Colab
- https://colab.research.google.com/drive/1DhSP8hE7rLCdqUYmxBsey5cCOd59eeIW?usp=sharing
---
### What is NER?
- NER stands for **Named Entity Recognition**.
- It is used in **Natural Language Processing (NLP)** to find and label **important words** or **phrases** in a sentence that are **names of people**, **places**, **dates**, **organizations**, etc.
---
### Why is NER important?
- Helps machines **understand key information** in text.
- Used in **chatbots**, **news analysis**, **search engines**, etc.
- Helps in **extracting structured data** from raw text.
---
### Common Entity Types

| **Entity Type** | **Meaning**                         | **Example**               |
| --------------- | ----------------------------------- | ------------------------- |
| **PERSON**      | Name of a person                    | Jeff Bezos, Elon Musk     |
| **ORG**         | Organization                        | Google, Microsoft         |
| **GPE**         | Geopolitical Entity (City, Country) | Canada, New York          |
| **DATE**        | Date                                | 17th February 2025        |
| **TIME**        | Time                                | 4 PM, 12:00 noon          |
| **MONEY**       | Monetary values                     | ₹8000, \$200              |
| **LOC**         | Location (non-political)            | Himalayas, Mount Everest  |
| **FAC**         | Facility                            | Airport, The Eiffel Tower |
| **PRODUCT**     | Product                             | iPhone, Tesla Model S     |

---
### Example Sentence :
`"Elon Musk founded Tesla in California in 2003."`

- **Detected Entities :**
  - `Elon Musk` → PERSON
  - `Tesla` → ORG
  - `California` → GPE
  - `2003` → DATE
---
### Required Python Packages
- **`spacy`**
---
### How the Code Works -
- **Input :**
```
text = "Apple Inc. unveiled the iPhone 12 at an event in Cupertino on October 13, 2020."
```
- **Output :**
```
Apple Inc. → ORG
Cupertino → GPE
October 13, 2020 → DATE
```
### Additional Insights :
- NER can be used to extract resumes, emails, legal documents, etc.
- spaCy, NLTK, and StanfordNLP are popular libraries for NER.
- NER also works in **many languages**, not just English.
---
