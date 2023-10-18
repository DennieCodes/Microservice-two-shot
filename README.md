# Wardrobify

Wardrobify is a Django backend application which provides several microservices to interact with three backend databases so that users can manage their collections of shoes and hats.  The project runs these microservices using Docker with the frontend served in React.

Team:

* Anthony Spence - Hats
* Dennie Chan - Shoes

## Design

### Screen shot of the project home page
![](images/Wardrobify.png)

### Diagram of the project folder structure
![](images/Microservice_diagram.png)

## Shoes microservice

### React view of shoes from shoes microservice
![](images/Shoe-list.png)

### React form for adding shoes through the shoes microservice
![](images/Shoe-form.png)

**MODEL**

For the Shoes microservice, we had one primary model with the following properties:

**model name**: The name of the shoe model

**manufacturer name**: The name of the shoe manufacturer

**color**: The color of the shoe

**picture url**: A link to a picture of the shoe

**assigned bin**: A foreign key which retrieves Bin information from the wardrobe microservice through polling.

**ENDPOINTS**

These are the endpoints that we were calling from our React app for our Shoes microservice

**GET** http://localhost:8080/api/shoes
**POST** http://localhost:8080/api/shoes/
**DELETE** http://localhost:8080/api/shoes/{shoe_number}
**GET** http://localhost:8100/api/bins/

## Hats microservice

### React view for the HatsList function
![](images/Hat-list.png)

### React view for the HatForm to create a new hat
![](images/Hat-form.png)

Used React Router to route the front end for the Nav Links and also linked the HatsForm to the HatsList.


**MODELS**
This model was setup to store hat style, color, fabric, and an image. Also utilized
Foreign Key in the models for the locationVO


**ENDPOINTS**

These are the endpoints that we were calling from our React app for our Hats microservice
**GET** http://localhost:8090/api/hats/
**POST** http://localhost:8090/api/hats/
**DELETE** http://localhost:8090/api/hats/3/
**GET** http://localhost:8100/api/locations/