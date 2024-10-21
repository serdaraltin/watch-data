# Explanation
This project purposes analyze data of camera with many modular detectings in real time.
This respostoriy includes model side of the project. Does detect with machine learning models and send datas to database.

# Preparation

** Prerequisite: Python 3.11.6 **

Yolov8n Model Link : ...
**"modules/detect/person/model"**

Gender Model Link : ...
The gender model path  : **"modules/detect/gender/model/genderv1e100.pth"**

Video Link :
The viideo path : **"tests/video"**

**Library  :**
```
pip install -r docs/requirements.txt
```
**Run  :**
```
python run_test.py
```

# MODULE CONTROL
You can control module status are whether enable or disable.
Just change module values in **config/json/config.json** !
Right at the bottom code block has 3 module active.
```
"module":{
            "detect":{
                "enter_exit": true,
                "gender": true,
                "age": true
            }...}
```

If Gender module is enable , it needs GPU to run. If you have GPU you can change device setting as gpu in **config/json/config.json** :

```
    "setting": {
        "debug": true,
        "device_": {
            "type": "gpu",
            "switch": true
        },
        "device": "gpu",
        "network": {
            "host": "127.0.0.1",
            "port": 5000,
            "backend": {
                "host": "127.0.0.1",
                "port": 3000}...}}
```


# app Folder

### main.py :

 The script configures Flask app which is web app. It imports some configuration setup from "config".
It includes keyboard event handling, particularly listening for a specific key press (like 'q') to perform actions like terminating processes.

# config Folder
 As config known it contains all necessary configurations here. Like factors that able to change.
Regarding this the config.json is a data file that holds the configuration details and the config_manager.py script define the settings in config.json.

## json
### config.json
 It includes settings device information, debug mode, network configurations(like host and port for both the main service and backend), database details, model files information. In addition there is "processing" to see a video process on window for testing purpose. "module" sub-key adresses models whether is enable or disable to able to control the project.

### config_manager.py
* **FRESH_CONFIG** : Dictionary represents a set of default configuration settings before the actual configuration is loaded from config.json. The actual file paths are gonna load by Config class.

As you can see the **preset** dictionary setting defined empty first.  It will fill as follow when "self.setting" attributes that loading the configuration and then creating a Setting object calls.

* **Present Class** : Prepared a user-friendly infrastructure for checking the existence of files and folders in the Config class. and then this class was converted into a value to uses in Config class.

**__dict__** adding all key-value pairs from that dictionary as attributes to the object and **__repr__** control the representation of objects and dynamically manage their attributes.

```python
def __repr__(self):
    return repr(self.__dict__)
```

* **Config class** : in summary checks files existing whether or not.

with **dump()** writes the current configuration (stored in self.__dict__) to config.json. It open **config.json** file by using **preset** dictionary essentially. This allows for persisting any runtime changes to the configuration. Before that

with **load()** The load method reads the configuration from config.json. It checks files existing and if its not , it calls **dump()** function. And then writes the default configuration (fresh_data) to the file and returns it.

```python
def load(self):
    # Dosyanın var olup olmadığını kontrol et
    if not os.path.exists(self.CONFIG_PATH):
        self.dump(fresh_data=True)
        return FRESH_CONFIG
```
After that it open the file and check if there is any space in the path it renewes. Finally the json file loads and returns.

 

```python
def __init__(self):
    self.__dict__ = self.load()
    self.setting = self.Setting(self.__dict__["setting"])

def __repr__(self):
    return repr(self.__dict__)
```

* **Setting class**:
 The Setting class provides a structured and modular way to manage different aspects of the project's settings.
As you can see code at the top the constructor of the Setting class takes a dictionary (value) as an argument, which represents the "setting" section of the configuration data. Inside the constructor, it assigns this dictionary to **self.__dict__**. By assigning the dictionary to self.__dict__, the keys of the dictionary become directly accessible as attributes of the Setting object.

 There are further nested classes (Network, Model, Processing, Module) for managing specific subsections of the configuration.
Each of these nested classes is initialized with the corresponding part of the configuration dictionary.
```python
class Setting(object):
    def __init__(self, value):
        self.__dict__ = value
        self.network = self.Network(self.__dict__["network"])
        ...
```
If nested classes , which is like Networks , has a subsets within itself , they are also initiliazed with their respective parts of the 'value' dictionary.

The configuration keys are directly accessible as attributes.
For instance in gender.py :

```python
model_name, model_type = config.setting.model.detect["gender"].values()
```
# interfaces Folder
 It contains common functions as abstract methods. It related with model folder.

### interface_base.py
 It includes the basic abstracts method functions that  must given from where it calls.
IBase abstract class has abstract methods that are '__str__','__repr__' , properties are : Id , createdAt , updatedAt. It should return a string that represents the object. It using at "interface_camera.py" and " interface_person.py".

### interface_camera.py
 Properties for camera-specific attributes like branch_id, model, resolution, install_date, status, and streaming_url.

### interface_person.py
Defines the IPerson and IEnterExit extending IBase.
* IPerson: Manages attributes for detected persons, like camera_id, detection_time, label, and confidence.
* IEnterExit: Tracks entry and exit events with properties like person_id, event_time, and event_type.
* IGender , IAge, IMovement: Manage gender detection, age range, and movement information for each person.

### interface_statistic.py
 The IStatstic's each properties must use when it used by another class. Properties are : enter, exit, female, male , total, current, current_female, current_male.
 For now it uses only by models/model_statistic.py.
 
**USAGE**
for exp in model/model_statistics.py :
```python
.
.
@property
def current(self):
    return self.enter - self.exit
.
```

* **push() :**
 It used to record new occurrences, like a person entering, or to add new data points to the statistical analysis.
**push** calls every time a person is detected, adding that event to a log of all detected persons.

**USAGE**
for exp in model/model_statistics.py :
```python
def push(self, person: Person):
    self.persons.append(person)
```

* **pop() :**
It uses to remove and return the last element.

**USAGE**
for exp in model/model_statistics.py :
```python
def pop(self) -> Person:
    return self.persons.pop() if self.persons else None
```
* **filter_by_key() :**
Considering its not using actively This method is intended to allow filtering of statistical data based on a particular key or criterion.

# Lib Folder
It contains common functions and baseline(gender model architecture).

## GUI
 Its totaly about to video window.

### lib/gui/drawing.py
 It is about the drawings on video window when opened.
Like door line , person information panel, person rectangle ...

### lib/gui/window_video.py
 It only includes one function that can open the video on screen.
If you don't want to see video processing on screen you can change status with config.json.
```
processing": {
            "show_window": true,
            ... }
```
## MATHEMATIC

### lib/mathematic/functions.py
* **is_crossing_line():**
 To find direction when a person cross the line. So figured out the person entered or left.

**parameters**
line_start, line_end, enter_direction information comes from **config.json**.
```
 "point_data": {"points": [
                            [472,352],
                            [698,352]
                          ],
                        "threshold_time": 5,
                        "enter_direction": [0,1]
                    }
```
prev_point, curr_point comes from **detect/person/person.py**
Do track the detected person. and track[-2] is prev_point, track[-1] is curr_point.
**USAGE**
```
 is_crossing_line(track[-2], track[-1], self.line_end, self.line_start, self.enter_direction)
```
# model Folder
 It contains the abstract classes that modules must use. 

### model_camera.py
 It created the configuration of the camera data going to the database with abstract.
Some of them are interited subclasses from *interfaces/interface_camera.py*.

### model_person.py
 It has person's informations. Like IPerson, IEnterExit, IGender, IAge, IMovement which are comes from *interfaces/interface_person.py*.
Every detected person has those informations to send to database.

**USAGE**
modules/detect/person/person.py :
```
model_enter_exit = EnterExit(
                                person_id = 1,
                                event_time = current_time.isoformat(),
                                event_type = method
                            )
person_example = Person(
                                age=model_age,
                                gender=model_gender,
                                enter_exit=model_enter_exit,  # here then
                                camera_id=1,
                                detection_time=current_time.isoformat(),
                                label="person",
                                confidence=0.85)
data = person_example.to_dict()
                          
                            self.queue_database_write(data)
```

### model_statistic.py
 It contains informations that uses on video window statistic panel.
It takes inhereted abstract class from *interfaces/interface_statistic.py* and adjust returnings.

```
# e.g :
@property
def enter(self):
    return sum(1 for p in self.persons if p.enter_exit.event_type == 'enter')
```
**USAGE**
modules/detect/person/person.py :

```
from lib.gui.drawing import draw_person_informations

draw_person_informations(annotated_frame, self.statistics.enter, self.statistics.exit, self.statistics.female, self.statistics.male, self.statistics.current_female, self.statistics.current_male)
```

# modules Folder
The all modules reqirements keeping here.

## DETECT
The *Detect* folder is a where the modules perform the detection operations. It includes existing modules we can provides for now which is Counter Person , Detect Gender.
### person.py :
Its where includes person detecting and all process. Let see in detail !
* **class PersonCounter()** :
In the structure funciton it takes necessary values from *config_manager.py*.
```
model_name, model_type = config.setting.model.detect["person"].values()
model_path = os.path.join('modules/detect/person/model', f"{model_name}.{model_type}")
```
Here is to get model file for person from config.
```
"person": {
            "name": "yolov8n",
            "type": "pt"
          }
```
and the other values...

Some convert class to object. Like
```
self.track_history = defaultdict(lambda: [])

```
Notes about Database values :,
self.db_write_queue:  queue is used to store data that needs to be written to a database.

self.flush_interval: This variable is set to 10 seconds

self.timer: This is a threading Timer object. It is used to periodically trigger the self.flush_database function after every self.flush_interval seconds. This ensures that the data in the queue is regularly written to the database.

* ** write_database()  : **
It processes and sends the data to be sent to the PostgreSql database.

* **flush_database() :**
This function is responsible for flushing (writing) the data from the queue to the database once in a <flush_interval> sec.

* ** queue_database_write()  :**
This function is used to add data to the queue (self.db_write_queue) for later writing to the database. Data passed to this function will be queued and eventually flushed to the database when the timer triggers the self.flush_database function.

* ** process_frame()  :**
It is the function that processes frames sended from the start function.
The incoming frame detects people by yolov8. Then identifies boxes and id.
It keeps track of every id that puts in the rectangle. The person tracking checks wheter the person enter with **is_crossing_line** function that imported.
If is_crossing_line returns True start additional process.
```
if len(track) > 1:
                    crossing_result = is_crossing_line(track[-2], track[-1], self.line_end, self.line_start, self.enter_direction)
                    if crossing_result is not False:
```

To able to detec gender of the person, it uses "predictions" function from detect/gender/gender.py.
This fuction return boolean value. For female its 0, for male its 1.
More information of "PredGender" mentioned at the down below of this description.
```
self.gender_pred = PredGender()
gender = self.gender_pred.predictions(annotated_frame, x_left, y_top, x_left + int(w), y_top + int(h))
model_gender = Gender(
                                person_id = 1,
                                gender = gender,
                                confidence = 0.5
                            )
```
"model_enter_exit" value, "model_gender" value, "model_age" value transformed to "person_example". These values define with abstract classes from *model_person.py*.
```
person_example = Person(
                                age=model_age,
                                gender=model_gender,
                                enter_exit=model_enter_exit,
                                camera_id=1,
                                detection_time=current_time.isoformat(),
                                label="person",
                                confidence=0.85)
```
It transforms to model_statictic.py to give information on statistic panel on video window.
It transforms to Database in json format as well.

Then there is some drawing process and delete tracking history.
At the end of the function draw_person_information write statistic panel.
"show_window" shows us the panel.

* start()   :
It takes the video that send to. Every frame checking and if its exist it sent to "process_frame". 

### gender.py   :
It is a where gender detection is performed through a trained data set.

* init ():
Firstly the model file path takes using with config.

**custom_config dict{}** :
This dictionary contains the custom settings necessary for configuring and initializing the model. These settings include ;

Model Settings ("model"): Defines the resizing and other parameters of the model. For instance, the "resize" setting (224, 224) indicates that the input images will be resized to these dimensions. "model_kwargs" contains additional arguments for configuring the model.

Utility Settings ("utils"): Defines utilities such as the file path where the model weights will be loaded from.

Load Model Weight ("load_model_weight"): If True, it loads the model weights from the specified path.

Mean and Standard Deviation ("mean" and "std"): The mean and standard deviation values used for image normalization.

**normalize** :
normalize performs the normalization process on the image before processing it. This prepares the images for processing by the model. It does this by scaling the image data according to certain mean([0.485, 0.456, 0.406]) and standard 8[0.229, 0.224, 0.225]) deviation values.

**test_transform**  :
test_transform defines a series of operations that preprocess the images to be input to the model.
Resizing: Resizes the image to the input dimensions of the model.
Converting to Tensor: Converts the image to a PyTorch tensor.
Normalization: Uses the aforementioned normalize function to normalize the image.

These processes ensure that the input images are in the correct format for the model to make accurate and consistent predictions.

DeepMAR_Resnet50 :
Im gonna mention that seperately first then why these 2 learning architecture using together.

DeepMAR is a model designed specifically for multi-attribute recognition tasks. "Mar" here means "Multi-Attribute Recognition". This model is usually used to recognize various characteristics of people,such as gender, clothing style, hairstyle...

Resnet50 is a 50-layer neural network architecture. Thanks to its deep layer structure, it can detect complex patterns and structures in images.

Here, the ResNet50's powerful feature extraction capability is combined with DEEPMAR's specialized needs in multi-attribute recognition tasks.

The model weight file(pth) puts in DeepMAR_Resnet50 structure.
```
self.model = DeepMAR_ResNet50(**custom_config["model"]["model_kwargs"])
```
Model weights (.pth file), which allows these 2 models to make effective predictions that can be used immediately.

The model weight file load according to the state of being active. 

* prediction()    :
It uses for "predictions" function from another python files.
If you set person frame coordinates and self frame you can get a gender boolean value which is 0 = female ,1 = male.
Ofcourse firstly the frame is processed and normalized. After put the model and get score.
score[0,0] refers gender label. First label is gender, and there is another labels if we'd like to use.

## process
It contains a modula starter function using by run_test.

# database Folder
We use PostgreSql as actual database. As PostgreSQL known its a server-based relational database system. All informations sends to there. Sqlite is just a built-in database system that we think as backup.

## connector :

### connector_postgre.py :
Contains scripts or modules that establish connectivity with the database.
There is only PersonDatabase Class bcs we just detect for persons.
It uses SQLAlchemy lib provides a nice “Pythonic” way of interacting with databases.

It inludes functions at the down below...

* init()    :

- It takes information of database's from config firstly.
- Then "DATABASE_URL" is created with this information. Format : "dialect+driver://- username:password@host:port/database"
- The create_engine function creates a database connection engine using this URL.
- "session" defines how to create sessions that are used to manage database operations. It is taken an object then.
**Note:** 
bind=engine: Bu argüman, sessionmaker'a oluşturulan oturumların hangi engine ile bağlantılı olacağını belirtir. Yani, bu oturumlar belirtilen engine üzerinden veritabanıyla etkileşimde bulunur.

Dictionary groups have been created with the data to be sent until "commmit" function.

They can use common values like person_id.
The exist dictionaries is commited to related DB that created in *database/model/model_postgre.py*.
**USAGE**
```python
modules/detect/person/person.py :
def write_database(self, data):
        self.PersonDataDB.set_data(data)
        self.PersonDataDB.commit()
```
### connector_sqlite.py :
* SQLiteConnector Class :
`SQLiteConnector` class inherits from `DatabaseInterface` and provides methods to interact with an SQLite database. It includes functionalities to connect to the database, perform CRUD (Create, Read, Update, Delete) operations, and close the connection
`SQLiteConnector` initializes the connection to the SQLite database using the provided database path. It also defines a sample table structure with columns `id`, `name`, and `value`

 **Methods**
**connect()
Establishes a connection to the SQLite database.

**close()
Closes the connection to the database.

**insert(data)
Inserts a new record into the database. data should be a dictionary, e.g., {'name': 'example', 'value': '123'}.

**update(conditions, new_values)
Updates records in the database. Both conditions and new_values should be dictionaries.

**delete(conditions)
Deletes records from the database. conditions should be a dictionary.

**select(conditions=None)
Retrieves records from the database. conditions is an optional dictionary to specify which records to retrieve. If conditions is not provided, all records are fetched.


## controller :
...
## dumps :  ??
It includes SQLite database files, containing the actual data stored in a structured format.
Contains backup or export files of the database. These are used for data recovery, migration, or analysis purposes.

## interface :
Houses components related to the user interface or API interfaces. This could include RESTful API endpoints, GraphQL schemas, or other interface-related code.

###interface_database.py :
 Its an abstract base of sqlite. Its necesssary for every database methods such as connect, close, insert, update, delete, and select(these have been mentioned at the top). The abstract classes are existing for unit-test actually. Its gonna checked by tests always, is there any missing or mismatch.

## model:
 Contains data models or schemas. These files define the structure of the data within the database, including table definitions, relationships, and other database schema details.

### model_postgre.py :
The `model_postgre.py` file contains four models: `PersonDB`, `EnterExitDB`, `GenderDB`, and `AgeDB`. These models are mapped to tables in a PostgreSQL database and are used to interact with the database in an object-oriented manner.

Every tables has name, specific columns, column's types, key type.
It uses by database/connector/connector_postgre.py. 


### data.sqlite :
A SQLite database file. This file holds the actual data in a structured, relational format, and is accessed by the developers to retrieve or store information.

If define all database connect way :
```
interfaces_database.py---> connector_postgre.py---> session
                                  ^
                                  |
                                  |
                            (model_postgre.py)---> #person = PersonDB(**self.get_person_data())
                                  ^
                                  |
                                  |
**data** in person module(person.py)
```
# test Folder
 These tests ensure classes, folders, files as expected by using Python's `unittest` framework.
```bash
python -m unittest <test_file_name>.py
```
### unittest.py
The `unittest.py` file contains the `Config` class, designed to handle test configurations using preset settings. This class is utilized across various test files to maintain consistent configuration settings for unit tests.

- Features of Config Class
**Initialization**
 The `Config` class initializes with preset settings, making these settings available to other test classes.

**Methods**
* ** `__repr__()`:** Returns a string representation of the `Config` instance (currently not implemented).
* ** `get_config_path()`:** Returns the path to the configuration file by combining preset folder and file settings.
* ** `read_preset()`:** Returns the preset settings.

**Usage**

The `Config` class is used in unit tests to access and utilize common configuration settings and paths. This ensures consistent configuration across various test files.

Usage in other test files: Each test file typically contains one or more test case classes like TestChecker, each focusing on different parts of your application. For example, you might have TestChecker for testing functionality related to data validation, another test case class for database-related tests, and so on...

```python
#e.g.
class TestChecker(unittest.TestCase):

"""if you have a method named test_example in the TestChecker class, unittest will recognize this as a test case to execute."""
```

### test_camera.py
 The test file contains a series of unit tests for the `Camera` class from model folder , which is used to represent camera devices in the system. 
 Created a sample data first for use in all test methods.
 ```python
 def setUp(self):
        # Ornek veri ile sinifin baslangic durumunu ayarla
        self.camera_instance = Camera(branch_id=1, model='XYZ', resolution='1080p', install_date=datetime.now(), status='active', streaming_url='http://example.com/stream', streaming_protocol='RTSP')
  ```
 * **setUp() :**
 Initializes a `Camera` instance with sample data for use in all test methods.

* **test_initialization_with_kwargs() :**
 Tests the initialization of the `Camera` instance with keyword arguments.
 Verifies that each property of the class is correctly set during initialization.

* **test_id_property() :**
 Tests the getter and setter methods for the `id` property of the `Camera` class.

* **test_branch_id_property() :**
 Tests the getter and setter methods for the `branch_id` property.

* **test_model_property() :**
 Tests the getter and setter methods for the `model` property.

* **test_resolution_property() :**
 Tests the getter and setter methods for the `resolution` property.

* **test_install_date_property() :**
 Tests the getter and setter methods for the `install_date` property.

* **test_status_property() :**
 Tests the getter and setter methods for the `status` property.

* **test_streaming_url_property() :**
 Tests the getter and setter methods for the `streaming_url` property.

* **test_streaming_protocol_property() :**
 Tests the getter and setter methods for the `streaming_protocol` property.

* **test_created_at_property() :**
 Tests the getter and setter methods for the `createdAt` property.

* **test_updated_at_property() :**
 Tests the getter and setter methods for the `updatedAt` property.

* **test_repr() :**
 Tests the `__repr__` method to ensure it returns the correct string representation of the `Camera` instance.

### test_checker.py 
 The test file contains a series of unit tests for the `Checker` class, which is part of the `services` module. The `Checker` class is designed to perform various system, network, and database checks. These tests cover file and folder existence, permissions, image model validation, port availability, API accessibility, IP address validity, system timezone, and database connection.

**TestCameraConcretecClass**
* **setUp() :**
 Initializes a `Checker` instance to be used in all test methods.

* **test_check_file_existence() :**
 Tests the method that checks for the existence of a file.
 Uses a temporary file to ensure the method correctly identifies that the file exists.

* **test_check_folder_existence() :**
 Tests the method that checks for the existence of a folder.
 Uses a temporary directory to ensure the method correctly identifies that the folder exists.

* **test_check_permissions() :**
 Tests the method that checks file permissions.
 Uses a temporary file to ensure the method correctly reports the file permissions.

* **test_check_image_model() :**
 Tests the method that checks the existence of an image model.
 Requires specifying the actual model file path for accurate testing.

* **test_check_port_availability() :**
 Tests the method that checks the availability of a network port.
 Requires specifying the actual host and port number for accurate testing.

* **test_check_api_accessibility() :**
 Tests the method that checks the accessibility of an API.
 Requires specifying a real API URL for accurate testing.

* **test_check_ip_validity() :**
 Tests the method that validates IP addresses.
 Checks both valid and invalid IP addresses.

* **test_check_system_timezone() :**
 Tests the method that checks the system's timezone setting.

* **test_check_database_connection() :**
 Tests the method that checks database connectivity.
 Requires setting up actual database connection details for accurate testing.

 ### test_config.py
The test file contains two test classes: `TestConfig` and `TestPreset`. These classes contain unit tests for the `Config` and `Preset` classes, respectively. The `Config` class tests verify that configuration settings are loaded properly, while the `Preset` class tests ensure that preset paths and types are set correctly.
**TestConfig Class**
- **setUp():** Initializes an instance of the `Config` class.
- **test_config_loading():** Tests whether the `Config` class is instantiated correctly.
- **test_network_settings():** Verifies that network settings (like host and port) are loaded correctly.
- **test_model_settings():** Checks if model settings (such as name and type) are properly loaded.
- **test_debug_settings():** Ensures that debug settings are correctly loaded.
- **test_device_settings():** Tests whether the device setting (e.g., 'gpu') is loaded correctly.
- **test_processing_settings():** Checks if processing settings (like source) are loaded properly.

**TestPreset Class**
- **setUp():** Initializes an instance of the `Preset` class.
- **test_preset_file_paths():** Tests if file paths in `Preset` (like 'config.json') are set correctly.
- **test_preset_folder_paths():** Verifies that folder paths (like 'config/json') in `Preset` are set correctly.
- **test_preset_response_types():** Checks if response types in `Preset` are set correctly.
- **test_preset_additional_folders():** Ensures that additional folder paths in `Preset` are correctly set.

### test_database.py
The test file contains a series of unit tests for the `SQLiteConnector` class, which handles SQLite database operations. The tests cover connection to the database, inserting, updating, deleting, and selecting records.

*Test Setup and Teardown*
* **setUpClass():**
 Initializes a temporary database for testing purposes.
 Creates an instance of the `SQLiteConnector` class with the temporary database.

* **setUp():**
 Establishes a database connection before each test.

* **tearDown():**
 Closes the database connection after each test.

* **tearDownClass():**
 Deletes the temporary database file after all tests are completed.

*Test Cases*

* **test_connection():**
 Tests whether the database connection is successfully established.

* **test_insert():**
 Tests the insertion of a record into the database and verifies that the record is correctly added.

* **test_update():**
 Tests updating a record in the database and checks if the update is reflected correctly.

* **test_delete():**
 Tests the deletion of a record from the database and confirms that the record is removed.

* **test_select():**
 Tests selecting records from the database. Inserts a test record and then attempts to retrieve it to verify the selection operation.

### test_models.py
 The test file contains several test classes, each targeting a specific model entity class. These tests cover the initialization of instances, getters and setters for properties, and the correct functionality of additional methods like `__repr__`.

*Test Setup and Teardown*

* **setUpClass():**
 Initializes a temporary database for testing purposes.
 Creates an instance of the `SQLiteConnector` class with the temporary database.

* **setUp():**
 Establishes a database connection before each test.

* **tearDown():**
 Closes the database connection after each test.

* **tearDownClass():**
 Deletes the temporary database file after all tests are completed.

*Test Cases*

* **test_connection():**
 Tests whether the database connection is successfully established.

* **test_insert():**
 Tests the insertion of a record into the database and verifies that the record is correctly added.

* **test_update():**
 Tests updating a record in the database and checks if the update is reflected correctly.

* **test_delete():**
 Tests the deletion of a record from the database and confirms that the record is removed.

* **test_select():**
 Tests selecting records from the database. Inserts a test record and then attempts to retrieve it to verify the selection operation.

# run_test.py
 The script is the entry point of the application. It initializes and starts processes, manages data flow, and ties together different modules like model processing (`model_statistic`, `model_person`), database operations (`connector_postgre`), and multiprocessing.

**Key Components**

* Multiprocessing
   The script uses the `multiprocessing` module to start the `person_counter_process`. This process is responsible for counting people, presumably using some form of image processing or data analysis.

* Model Processing
 The script involves different models from the `model` package, such as `Statistic`, `Person`, `EnterExit`, `Gender`, `Age`. These models are likely used for data processing and statistical analysis.

* Database Interaction
  `connector_postgre.PersonDatabase` is used for interacting with a PostgreSQL database. This includes operations like data insertion or updates based on the person counting and analysis.

* Configuration
  The script uses a configuration module (`config`) to manage settings and parameters, which may include database connection details, model parameters, etc.

* Data Handling
  An example data dictionary is provided, which seems to structure data related to person detection, gender analysis, and entry/exit events.


