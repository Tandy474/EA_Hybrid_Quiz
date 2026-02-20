# EA Hybrid Quiz

# Introduction
The Environment Agency(EA) operates across a wide range of environmental, regulatory, and operational domains, including flood risk management, pollution response, permitting, environmental monitoring, and incident management.  Staff and delivery partners must maintain a consistent baseline knowledge to ensure safe, compliant, and effective operations.  This includes understanding EA policies, procedures, environmental principles, and technical concepts relevant to decision-making.  In such a multidisciplinary environment, accessible digital learning tools play an important role in supporting competence, onboarding, and continuous professional development.

The EA Hybrid Quiz is an interactive learning application designed to strengthen staff understanding of key EA Topics.  The tool provides a structured quiz experience that can be used for training, induction, toolbox talks, or self-directed e-learning.  The (MVP) minimum viable product includes a login system, category and difficulty selection, question presenting optional answer validation, and instant feedback.  The quiz content can cover EA Basics, Flooding, Pollution, Regulation, or mathematical knowledge relevant to EA roles.

A key feature of this project is the hybrid interface approach, offering two front-end options:
  TKinter: a desktop-style GUI suitable for local use on EA laptops.
  Strealit: a browser-based interface ideal for demonstrations, remote access, and rapid deployment.

Both interfaces read from the same CSV-based data store, ensuring consistency and ease of maintenance.  The project uses Python and object-oriented programming principles, with classes for questions, quiz management, and authentication.  The system includes exception handling, input validation, and testable logic, supported by automated unit tests.

For the EA, this MVP is relevant because it provides a low-cost, accessible, and easily maintainable tool that supports organisational competence. The Hybrid design also demonstrates modern development practices, version control, documentation, and continuous integration, aligning with professional software engineering standards.

## Design Section
### Figma-style GUI design
<img width="931" height="772" alt="image" src="https://github.com/user-attachments/assets/f11d80de-d61f-4363-982a-37f248ced35d" />

## Requirements Table
### Functional Requirements Table
| ID   | Requirement |
| ---- | ----------- |
| FR1  | System must authenticate users via CSV.  |
| FR2  | System must allow category selection.  |
| FR3  | System must allow difficulty selection.  |
| FR4  | System must load questions from CSV.  |
| FR5  | System must display questions and options.  |
| FR6  | System must validate answers.  |
| FR7  | System must show correct/ incorrect feedback.  |
| FR8  | System must show final score.  |
| FR9  | System must support both TKinter and Streamlit interfaces  |


### Accessibility Requirements Table
| ID   | Requirement |
| ---- | ----------- |
| AR1  | High-contrast colour scheme.  |
| AR2  | Keyboard navigation supported.  |
| AR3  | Text-based feedback(not colour only.  |
| AR4  | Large readable fonts.  |
| AR5  | Clear error messages.  |


### Non-Functional Requirements Table
| ID   | Requirement |
| ---- | ----------- |
| NFR1 | App should load within 2 seconds.  |
| NFR2 | CSV errors handled.  |
| NFR3 | Code must be modular and maintainable.  |
| NFR4 | Logic must be testable via unit tests.  |
| NFR5 | Must run on standard EA laptops without extra installation.  |


## Tech Stack Outline
  +**Language:** Python 3
  +**GUI Frameworks:**
    +TKinter (desktop)
    +Streamlit (Web)
  
+**Data Storage:** CSV files (

+**Libraries:**
    +CSV - reading/writing data
    + TKinter - GUI
   + Streamlit - Web interface
   + unittest - automated testing
   + dataclasses - Question model
    
+**Tools:**
   + GitHub - version control
   + Figma -  interface prototyping
   + Streamlit - Web interface
   + VS Code - development environment
    
    

## Testing Section
### A third-level heading

## Documentation Section

## Evaluation Section

## A second-level heading

## A second-level heading


## A second-level heading



6 Evaluation



