# e-commerce-pp5

Creating an E-commerce store for the project 5 of the code institute.

## Table of content

Here you can find all the content in the docs and links to each individual section.

-   [Clone and Test](#clone-and-test)
    -   [Cloning](#clone-repo)
    -   [Virtual enviroment](#virtual-enviroment-venv)
-   [Planning](#planning)
    -   [Site objective](#site-objective)
    -	[Features](#features)
	-	[Models](#models)
    -   [Wireframe](#wireframe)
    -   [Color](#color)
- [Business Model](#business-model)
    - [Marketing & Search Engine Optimisation (SEO)](#marketing--search-engine-optimisation-seo)
    - [Technologies used]()

> You will find a back to top link at the end of every section.

## Clone and Test

### Clone repo
To start cloning by following the steps below:

-   you will need the link provided by the following [github repo](https://github.com/jhoanTrujillo/e-commerce-pp5.git)
-   find the folder where you would like to clone the repo.
-   Use the `git clone` command follow by the link from the above step.

Once that is done you can use `pip3 install -r requirements.txt` to install the requirements globally in your computer.

If you would prefer to install the requirements in a virtual enviroment for the purpose of testing then follow the steps below.

### Virtual enviroment (Venv)
To run a virtual enviroment to test the app locally follow the steps below:

-   you will need to install python virtualenv package. By using the command `pip3 install virtualenv`
-   Once installed. Go to the root folder where the repo was cloned and run command: `python3 -m venv env`
-   Lastly, activate the enviroment created using the following console commands:
    -   On Mac: `source env/bin/activate`
    -   On Windows:
        -   CMD: `env/Scripts/activate.bat `
        -   Powershell: `env/Scripts/Activate.ps1 `

Once that is done, you should be able to run `pip3 install -r requirements.txt` to install the requirements without affecting your global enviroment.

[Table of content](#table-of-content)

---

## Planning

### Site objective
The pin selling platform aims to provide users with a diverse selection of high-quality pins, ranging from enamel pins to collectibles and custom designs. Committed to offering a curated collection that appeals to pin enthusiasts of all interests and tastes, the platform strives to create an engaging and enjoyable shopping experience.

In terms of the project, the objective is to test my knowledge of Django and to learn more about the full-stack development workflow using Django.

### Features
Below there is a list of features of the main functionalities I thought would be useful for users. They are rank by priority and ranked based on the MoSCoW method prioritisation.

<details close>
<summary>Feature list</summary>

| Feature | Importance | Difficulty | Priority |
|-------------------------|-------------|------------|-------------|
| **Account Features** | | | |
| Account login | 5 | 3 | Must have |
| Account logout | 4 | 2 | Should have |
| Account creation | 5 | 4 | Must have |
| Account deletion | 3 | 4 | Could have |
| Account/Profile update | 5 | 3 | Must have |
| User profile | 4 | 3 | Should have |
| Summary of orders | 4 | 3 | Should have |
| **Product Features (Site owner)** | | | |
| Product creation | 5 | 3 | Must have |
| Product update | 4 | 4 | Should have |
| Product deletion | 3 | 5 | Could have |
| **Product Features (users)** | | | |
| Product page | 5 | 4 | Must have |
| Product Collection | 5 | 3 | Must have |
| product reviews | 4 | 4 | Should have |
| **Cart/Checkout features** ||||
| Add product to cart | 5 | 3 | |
| Remove product from cart | 4 | 3 | Should have |
| See order summary | 4 | 2 | Could have |
| Pay and complete checkout | 5 | 4 | Must have |
| **Blog post (Site owner)** | | | |
| Blog post creation | 5 | 4 | Must have |
| Blog post update | 4 | 3 | Should have |
| Blog post deletion | 3 | 3 | Could have |
| **Blog post (users/registered)** | | | |
| Like post | 3 | 3 | Could have  |
| Comment creation | 4 | 3 | Should have |
| Comment update | 3 | 3 | Could have |
| Comment deletion | 3 | 4 | Could have |

</details>

### Models
A collection of all the data models.

<details close>
<summary>UserProfile</summary>

| Key               | Name                     | Type                |
|-------------------|--------------------------|---------------------|
| Foreign_Key       | User                     | ForeignKey          |
|                   | Default_Phone_Number     | CharField           |
|                   | Default_Country          | CountryField        |
|                   | Default_Street_Address1  | CharField           |
|                   | Default_Street_Address2  | CharField           |
|                   | Default_Town_or_City     | CharField           |
|                   | Default_County           | CharField           |
|                   | Default_Postcode         | CharField           |

</details>

<details close>
<summary>Collection</summary>

| Field             | Type       | Description                            |
|-------------------|------------|----------------------------------------|
| id                | Primary Key| Unique identifier for the collection.  |
| name              | CharField  | Name of the collection.                |
| user_friendly_name| CharField  | User-friendly name of the collection.  |
| description       | TextField  | Description of the collection.         |



</details>

<details close>
<summary>Product</summary>

| Field             | Type       | Description                            |
|-------------------|------------|----------------------------------------|
| id                | Primary Key| Unique identifier for the product.      |
| title             | CharField  | Title of the product.                  |
| description       | TextField  | Description of the product.            |
| sku               | CharField  | Stock Keeping Unit of the product.     |
| price             | DecimalField| Price of the product.                  |
| image             | ImageField | Image of the product.                  |
| image_url         | URLField   | URL of the image of the product.       |
| rating            | DecimalField| Rating of the product.                 |
| collection_id     | ForeignKey | Foreign key to Collection table.        |
| stock             | IntegerField| Stock quantity of the product.         |
| created_date      | DateTimeField| Date and time when the product was created.|
| updated_date      | DateTimeField| Date and time when the product was last updated.|


</details>

<details close>
<summary>Variant</summary>
| Field             | Type       | Description                            |
|-------------------|------------|----------------------------------------|
| id                | Primary Key| Unique identifier for the variant.      |
| product_id        | ForeignKey | Foreign key to Product table.          |
| title             | CharField  | Title of the variant.                  |
| price             | DecimalField| Price of the variant.                  |
| image             | ImageField | Image of the variant.                  |
| image_url         | URLField   | URL of the image of the variant.       |
| stock             | IntegerField| Stock quantity of the variant.         |
</details>

<details close>
<summary>Order</summary>

| Key               | Name              | Type            |
|-------------------|-------------------|-----------------|
|                   | Order_Number      | CharField       |
| Foreign_Key       | User_Profile      | ForeignKey      |
|                   | Full_Name         | CharField       |
|                   | Email             | EmailField      |
|                   | Phone_Number      | CharField       |
|                   | Country           | CountryField    |
|                   | Postcode          | CharField       |
|                   | Town_or_City      | CharField       |
|                   | Street_Address1   | CharField       |
|                   | Street_Address2   | CharField       |
|                   | County            | CharField       |
|                   | Date              | DateTimeField   |
|                   | Delivery_Cost     | DecimalField    |
|                   | Order_Total       | DecimalField    |
|                   | Grand_Total       | DecimalField    |
|                   | Original_Bag      | TextField       |
|                   | Stripe_PID        | CharField       |

</details>

<details close>
<summary>LineItem</summary>

| Key          | Name              | Type            |
|--------------|-------------------|-----------------|
| Foreign Key  | Order             | ForeignKey      |
| Foreign Key  | Product           | ForeignKey      |
| CharField    | Product_Size      | CharField       |
| TextField    | Selected_Options  | TextField       |
| IntegerField | Quantity          | IntegerField    |
| DecimalField | Lineitem_Total    | DecimalField    |

</details>

<details close>
<summary>DiscountCode</summary>

| Key               | Name       | Type        |
|-------------------|------------|-------------|
|                   | Code       | CharField   |
|                   | Description| TextField   |
|                   | Amount     | DecimalField|
|                   | Percent    | DecimalField|
|                   | Minimum Purchase | DecimalField|
|                   | Start Date | DateField   |
|                   | End Date   | DateField   |
|                   | Active     | BooleanField|

</details>

<details close>
<summary>Blog</summary>

| Key               | Name            | Type            |
|-------------------|-----------------|-----------------|
| Foreign Key       | User            | ForeignKey      |
|                   | Title           | CharField       |
|                   | Content         | TextField       |
|                   | Created Date    | DateTimeField   |
|                   | Updated Date    | DateTimeField   |

</details>

<details close>
<summary>Comment</summary>

| Key               | Name            | Type            |
|-------------------|-----------------|-----------------|
| Foreign Key       | User            | ForeignKey      |
| Foreign Key       | Blog            | ForeignKey      |
|                   | Content         | TextField       |
|                   | Created Date    | DateTimeField   |
|                   | Updated Date    | DateTimeField   |

</details>

[Table of content](#table-of-content)

## UX design 

### Wireframe
[wireframe files](https://github.com/jhoanTrujillo/e-commerce-pp5/tree/main/github_media)

### Color

**Selected colors**
| Hex | Title|
|-----|-------|
| #ffffff | White |
|#1C1932 |Midnight Black|
|#8C52FF |Royal Purple|
|#5CE1E6 |Aqua Sky|
|#FF5757 |Vivid Red|

In designing the color scheme for the e-commerce store, I aimed to infuse it with popping and energetic colors. The vibrant hues of Aqua Sky (#5CE1E6), Vivid Red (#FF5757), and Royal Purple (#8C52FF) were carefully selected to evoke a sense of dynamism and excitement, ensuring that visitors attention is catched.

Moreover, the chosen colors provide a great contrast between sections, facilitating navigation and enhancing visual hierarchy. Whether it's highlighting product categories or drawing attention to promotional offers, the distinct color palette ensures that each section stands out, guiding users seamlessly through their shopping journey.

### Fonts

In designing my online store, I chose the **Barlow** font family—Barlow and **Barlow Condensed**. These fonts are easy to read and strike a balance between friendly and professional. They fit perfectly with my tone—friendly but informative.

**Barlow and Barlow Condensed** go well together and make everything look neat and organized. With lots of different styles to choose from, like bold and regular, I can highlight important stuff without making it hard to read.

Basically, I picked the Barlow fonts because they help me make my online store easy to use and nice to look at. They make it simple for customers to find what they need and enjoy their shopping experience.

## Business Model

The operational model is straightforward. Our website serves as a platform for selling products directly to consumers, making it a B2C enterprise. Our dedicated team curates and adds new products to our inventory regularly. Customers have the freedom to browse, select items, and proceed to checkout seamlessly. We offer single purchases only.

Our mailing lists are cultivated from the email addresses collected via our newsletter signup form, conveniently located above the footer on our main page. This invaluable resource enables us to conduct targeted customer outreach and marketing campaigns effectively. Additionally, our Facebook business page serves as an interactive platform for sharing content with customers and fostering engagement through comments and messages.

### Marketing & Search Engine Optimisation (SEO)


**Keywords**
- Enamel pins
- Handcrafted pins
- Unique pins
- Lapel pins
- Pin badges
- Artisan pins
- Custom pins
- Collectible pins
- Trendy pins
- Fashion pins
- Cute pins
- Pop culture pins
- - Vintage pins
- Retro pins
- Whimsical pins
- Animal pins
- Floral pins
- Minimalist pins
- Statement pins
- Pin accessories






**Sitemap**

**Robot.txt**

### Technologies used

**Languages**
- HTML
- CSS
- JavaScript
- Python

**Frameworks and Libraries**
- Django
- Bulma CSS
- Stripe
