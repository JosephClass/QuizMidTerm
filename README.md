# PROJECT MID TERM

## Here is how to install this project:

### First

#### you need to download this git project 
#### write `git clone https://github.com/JosephClass/QuizMidTerm.git` in cmd to download this project

### Second
#### after you download the project,you can go to the folder of the project using cmd and write the text below
#### `pip install -r requirements.txt` if your python is python 2
#### `pip3 install -r requirements.txt` if your python is python 3

### Third
#### if you want to add file csv you can go to the main.py files
#### and go the `df = AccessData.import_csv("C:\\Users\\User-PC\\Desktop\\us-500.csv")` part and
#### change `"C:\\Users\\User-PC\\Desktop\\us-500.csv"` with your csv file location

### Fourth
#### and if you want to connect your local mysql dont forget to configure it in main.py file
#### espescially in `AccessData = CaseStudy.StudiKasus(host="localhost" , port=3306 , user="root" , password=os.environ['PASS_MYSQL'])` part
#### you need to change `os.environ['PASS_MYSQL']` with your mysql root password