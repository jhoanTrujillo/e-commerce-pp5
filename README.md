# e-commerce-pp5
Creating an E-commerce store for the project 5 of the code institute.

[Deployed project](https://ci-project-5-joe-pins-be851091e775.herokuapp.com/)

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
- [Deployment](#deployment)
    - [ElephantSQL Database](#elephantsql-database)
    - [Amazon AWS](#amazon-aws)
    - [heroku](#heroku)
- [Testing](#testing)
    - [Site Speed](#site-speed)
    - [Manual Testing](#manual-testing)
    - [Bugs](#Bugs)
- [Credits](#credits)

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
| product reviews | 4 | 4 | Could have |
| **Cart/Checkout features** ||||
| Add product to cart | 5 | 3 | Must Have |
| Remove product from cart | 4 | 3 | Should have |
| See order summary | 4 | 2 | Could have |
| Pay and complete checkout | 5 | 4 | Must have |

</details>

### Models
A collection of all the data models.

<details>
  <summary><strong>Collection Model</strong></summary>
  
  **Description:** The `Collection` model represents a group or category of products.
  
  | Field Name         | Field Type              | Description                                                                                           |
  |--------------------|-------------------------|-------------------------------------------------------------------------------------------------------|
  | name               | CharField(max_length=100) | The name of the collection.                                                                           |
  | image              | ImageField               | An image associated with the collection.                                                              |
  | user_friendly_name | CharField(max_length=100) | A user-friendly name for the collection.                                                              |
  | description        | TextField                | A description of the collection.                                                                      |

</details>

<details>
<summary><strong>Product Model</strong></summary>

**Description:** The `Product` model represents individual items available for sale in the store.

| Field Name    | Field Type                              | Description                                                                                      |
|---------------|-----------------------------------------|--------------------------------------------------------------------------------------------------|
| title         | CharField(max_length=100)               | The title of the product.                                                                        |
| description   | TextField                               | A description of the product.                                                                    |
| sku           | CharField(max_length=100, null=True)    | The stock keeping unit (SKU) of the product.                                                      |
| price         | DecimalField(max_digits=6, decimal_places=2) | The price of the product.                                                                   |
| image         | ImageField                              | An image associated with the product.                                                             |
| image_url     | URLField(max_length=1024, null=True)    | A URL link to an image of the product.                                                            |
| rating        | DecimalField(max_digits=6, decimal_places=2) | The rating of the product.                                                                |
| collection    | ForeignKey(Collection, on_delete=models.SET_NULL, null=True) | The collection to which the product belongs.                                        |
| stock         | IntegerField                            | The current stock level of the product.                                                          |
| created_date  | DateTimeField(auto_now_add=True)       | The date and time when the product was created.                                                  |
| updated_date  | DateTimeField(auto_now=True)           | The date and time when the product was last updated.                                             |
</details>

<details>
  <summary><strong>Variant Model</strong></summary>

  **Description:** The `Variant` model represents different variations or options for a specific product.

  | Field Name    | Field Type                              | Description                                           |
  |---------------|-----------------------------------------|-------------------------------------------------------|
  | product       | ForeignKey(Product, on_delete=models.CASCADE) | The product to which the variant belongs.      |
  | title         | CharField(max_length=100)               | The title or name of the variant.                     |
  | sku           | CharField(max_length=100, null=True)    | The stock keeping unit (SKU) of the variant.           |
  | price         | DecimalField(max_digits=6, decimal_places=2) | The price of the variant.                        |
  | image         | ImageField                              | An image associated with the variant.                  |
  | image_url     | URLField(max_length=1024, null=True)    | A URL link to an image of the variant.                |
  | stock         | IntegerField                            | The current stock level of the variant.               |

</details>

<details>
  <summary><strong>Contact Model</strong></summary>

  **Description:** The `Contact` model stores information about messages sent through the contact form.

  | Field Name | Field Type                     | Description                                      |
  |------------|--------------------------------|--------------------------------------------------|
  | sender     | CharField(max_length=100)      | The name of the sender.                          |
  | email      | EmailField(max_length=100)     | The email address of the sender.                 |
  | subject    | CharField(max_length=254)      | The subject of the message (optional).           |
  | message    | TextField                      | The content of the message.                      |
  | sent_at    | DateTimeField(auto_now_add=True) | The date and time when the message was sent.  |

</details>

<details>
  <summary><strong>Order Model</strong></summary>

  **Description:** The `Order` model stores information about customer orders.

  | Field Name      | Field Type                                        | Description                                                   |
  |-----------------|---------------------------------------------------|---------------------------------------------------------------|
  | order_number    | CharField(max_length=32)                          | The unique order number.                                      |
  | user_profile    | ForeignKey(UserProfile, on_delete=models.SET_NULL) | The user profile associated with the order (if applicable).   |
  | full_name       | CharField(max_length=50)                           | The full name of the customer.                                |
  | email           | EmailField(max_length=254)                         | The email address of the customer.                            |
  | phone_number    | CharField(max_length=20)                           | The phone number of the customer.                             |
  | country         | CountryField(blank_label='Country *')              | The country of the customer.                                  |
  | postcode        | CharField(max_length=20, null=True)                | The postal code of the customer.                              |
  | town_or_city    | CharField(max_length=40)                           | The town or city of the customer.                             |
  | street_address1 | CharField(max_length=80)                           | The first line of the street address of the customer.         |
  | street_address2 | CharField(max_length=80, null=True)                | The second line of the street address of the customer (if applicable). |
  | county          | CharField(max_length=80, null=True)                | The county or region of the customer (if applicable).         |
  | date            | DateTimeField(auto_now_add=True)                   | The date and time when the order was placed.                  |
  | delivery_cost   | DecimalField(max_digits=6, decimal_places=2)       | The cost of delivery for the order.                           |
  | order_total     | DecimalField(max_digits=10, decimal_places=2)      | The total cost of the order.                                  |
  | grand_total     | DecimalField(max_digits=10, decimal_places=2)      | The grand total cost of the order.                            |
  | original_cart   | TextField                                         | The JSON representation of the original cart contents.        |
  | stripe_pid      | CharField(max_length=254)                         | The payment ID provided by Stripe for the order.              |

</details>

<details>
  <summary><strong>ProductLineItem Model</strong></summary>

  **Description:** The `ProductLineItem` model represents line items associated with products in an order.

  | Field Name      | Field Type                                        | Description                                                   |
  |-----------------|---------------------------------------------------|---------------------------------------------------------------|
  | order           | ForeignKey(Order, on_delete=models.CASCADE)      | The order associated with the line item.                      |
  | product         | ForeignKey(Product, on_delete=models.CASCADE)    | The product associated with the line item.                    |
  | quantity        | IntegerField                                     | The quantity of the product in the line item.                |
  | lineitem_total  | DecimalField(max_digits=6, decimal_places=2)      | The total cost of the line item (calculated automatically).  |

</details>

<details>
  <summary><strong>VariantLineItem Model</strong></summary>

  **Description:** The `VariantLineItem` model represents line items associated with variants in an order.

  | Field Name      | Field Type                                        | Description                                                   |
  |-----------------|---------------------------------------------------|---------------------------------------------------------------|
  | order           | ForeignKey(Order, on_delete=models.CASCADE)      | The order associated with the line item.                      |
  | variant         | ForeignKey(Variant, on_delete=models.CASCADE)    | The variant associated with the line item.                    |
  | quantity        | IntegerField                                     | The quantity of the variant in the line item.                |
  | lineitem_total  | DecimalField(max_digits=6, decimal_places=2)      | The total cost of the line item (calculated automatically).  |

</details>

[Table of content](#table-of-content)

### Wireframe
[wireframe files](https://github.com/jhoanTrujillo/e-commerce-pp5/tree/main/github_media)

### Color
For ease of use I'm working with the colors that are provided by the bulma framework. This reduces the decision fatigue and ensure the color palette is always on theme. 

[Bulma color palette](https://bulma.io/documentation/features/color-palettes/)

### Fonts
In designing my online store, I chose the **Barlow** font family—Barlow and **Barlow Condensed**. These fonts are easy to read and strike a balance between friendly and professional. They fit perfectly with my tone—friendly but informative.

**Barlow and Barlow Condensed** go well together and make everything look neat and organized. With lots of different styles to choose from, like bold and regular, I can highlight important stuff without making it hard to read.

Basically, I picked the Barlow fonts because they help me make my online store easy to use and nice to look at. They make it simple for customers to find what they need and enjoy their shopping experience.

## Business Model
The operational model is straightforward. Our website serves as a platform for selling products directly to consumers, making it a B2C enterprise. Our dedicated team curates and adds new products to our inventory regularly. Customers have the freedom to browse, select items, and proceed to checkout seamlessly. We offer single purchases only.

Our mailing lists are cultivated from the email addresses collected via our newsletter signup form, conveniently located above the footer on our main page. This invaluable resource enables us to conduct targeted customer outreach and marketing campaigns effectively. Additionally, our Facebook business page serves as an interactive platform for sharing content with customers and fostering engagement through comments and messages.

### Marketing & Search Engine Optimisation (SEO)

At Joe's crazy pins, we aim to maximize our online presence and engage with our audience effectively through a strategic Facebook marketing plan. Here's how we plan to leverage Facebook to drive sales and foster customer relationships:

**Single Product Purchases**: Our focus is on promoting single product purchases, highlighting the unique features and benefits of each item to capture the attention of potential customers.

**Utilizing Facebook Marketing and Mailchimp Newsletter**: We will deploy targeted Facebook ads to reach our desired audience segments, ensuring our products are showcased to those most likely to make a purchase. Additionally, we'll complement our Facebook efforts with a regular newsletter sent via Mailchimp, providing subscribers with updates on our latest products, promotions, and industry trends.

**A/B Testing for Marketing Campaigns**: To optimize our marketing efforts, we'll conduct A/B testing on our Facebook ad campaigns. By testing different ad creatives, copywriting styles, and targeting parameters, we can identify the most effective strategies for driving engagement and conversions.

**SEO Optimization for Increased Discoverability**: In addition to our Facebook initiatives, we'll focus on SEO optimization to increase the discoverability of our brand and products in search engine results. By optimizing our website content, meta tags, and product descriptions with relevant keywords, we'll improve our visibility and attract organic traffic to our online store.

**Showcasing Facebook Page**: We'll prominently display a picture of our Facebook page on our website, inviting visitors to connect with us on social media. This will help us expand our online community and foster brand loyalty among our audience.

![facebook page for joe's crazy pins](https://raw.githubusercontent.com/jhoanTrujillo/e-commerce-pp5/main/github_media/facebook%20page.png)
> You can access the facebook page via the footer of the website or via .

Through these strategic initiatives, we aim to enhance brand visibility, drive sales, and cultivate lasting relationships with our customers on Facebook and beyond.

**Keywords**
To ensure optimal visibility in search engine results and attract the right audience to our website, we have identified a comprehensive list of keywords related to our products:

- Enamel pins
- Handcrafted pins
- Unique pins
- Lapel pins
- Pin badges
- Custom pins
- Collectible pins
- Trendy pins
- Fashion pins
- Cute pins
- Vintage pins
- Retro pins
- Whimsical pins
- Floral pins
- Minimalist pins
- Statement pins
- Pin accessories

By strategically incorporating these keywords into our website content, product descriptions, and meta tags, we can improve our search engine rankings and attract organic traffic from users actively searching for these terms. This will help us reach our target audience more effectively and increase the visibility of our products online.

**Sitemap**
I used XML Siteamaps to create a sitemap for the site. The sitemap is submitted to Google Search Console to help with SEO.

**Robot.txt**
Added a robots.txt file to the site to help with SEO. The robots.txt file is used to tell search engines which pages to crawl and which to ignore. Here is the content of the robots.txt file:

```
user-agent: *
disallow: /checkout/
sitemap: https://ci-project-5-joe-pins-be851091e775.herokuapp.com/sitemap.xml
```

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

## Deployment

### ElephantSQL Database

This project utilizes [ElephantSQL](https://www.elephantsql.com/) for the PostgreSQL Database.

To obtain your own PostgreSQL Database, sign up with your GitHub account, then follow these steps:

1. Click on "Create New Instance" to initiate a new database.
2. Provide a name (typically the name of your project, such as "e-commerce-pp5").
3. Choose the "Tiny Turtle (Free)" plan.
4. You can leave the Tags field empty.
5. Select the Region and Data Center that are closest to your location.
6. Once the database is created, click on its name to access the database URL and Password.

### Amazon AWS

This project utilizes AWS to host media and static files online, as Heroku does not persist this type of data.

Follow these steps to connect your project to AWS after creating an AWS account and logging in to the AWS Management Console:

#### S3 Bucket

1. Search for S3.
2. Create a new bucket, giving it a name (typically matching your Heroku app name), and choose the region closest to you.
3. Untick "Block all public access" and acknowledge that the bucket will be public (required for it to work on Heroku).
4. Enable ACLs and select "Bucket owner preferred" from Object Ownership.
5. From the Properties tab, enable static website hosting and specify "index.html" and "error.html" in their respective fields, then click Save.
6. In the Permissions tab, paste the provided CORS configuration.

```
[
 {
  "AllowedHeaders": [
   "Authorization"
  ],
  "AllowedMethods": [
   "GET"
  ],
  "AllowedOrigins": [
   "*"
  ],
  "ExposeHeaders": []
 }
]
```

7. Copy your ARN string.
8. In the Bucket Policy tab, use the Policy Generator to create a policy allowing GetObject actions.
9. Copy the generated Policy and paste it into the Bucket Policy Editor, ensuring to add /* to the end of the Resource key. It tends to look like this but it might be different depending on your needs.
```
{
 "Id": "Policy1234567890",
 "Version": "2012-10-17",
 "Statement": [
  {
   "Sid": "Stmt1234567890",
   "Action": [
    "s3:GetObject"
   ],
   "Effect": "Allow",
   "Resource": "arn:aws:s3:::your-bucket-name/*"
   "Principal": "*",
  }
 ]
}
```
10. Click Save.
11. In the Access Control List (ACL) section, click "Edit" and enable List for Everyone (public access), accepting any warning prompts.

If the edit button is disabled, ensure that ACLs are enabled in the Object Ownership section.

### IAM Setup

Follow these steps to set up IAM (Identity and Access Management) on AWS:

1. Create a New Group
   - Name: group-ci-project-5-joe-pins (group name + project name)
   - Tags (optional, but must be clicked to proceed to the review policy page)

2. Assign Permissions to the Group
   - Select the newly created group and navigate to the Permissions tab.
   - Open the Add Permissions dropdown and click Attach Policies.
   - Select the AmazonS3FullAccess policy and click Add Permissions.

3. Import Managed Policy
   - Select the Import Managed Policy link from the JSON tab.
   - Search for S3, choose the AmazonS3FullAccess policy, and then Import.
   - Paste your S3 Bucket ARN into the "Resources" key on the Policy.

4. Review and Create Policy
   - Review the policy details.
   - Name: ci-project-5-joe-pins (policy name + project name)
   - Description: "Access to S3 Bucket for ci-project-5-joe-pins static files."
   - Click Create Policy.

5. Attach Policy to Group
   - Select your "group-ci-project-5-joe-pins" from User Groups.
   - Click Attach Policy, search for "ci-project-5-joe-pins", and select it.

6. Create a New User
   - Name: user-ci-project-5-joe-pins (user name + project name)
   - Select Programmatic Access for "Select AWS Access Type".
   - Assign the user to the "group-ci-project-5-joe-pins".
   - Tags (optional, but must be clicked to proceed to the review user page).
   - Click Create User.

7. Download User Credentials
   - Download the .csv file containing the user's Access key ID and Secret access key.
   - Save a copy on your system immediately after download.

Ensure to securely store and manage the user's credentials:

`AWS_ACCESS_KEY_ID` = Access key ID
`AWS_SECRET_ACCESS_KEY` = Secret access key

## Testing Overview
Due to time constraints, resolving all testing issues within this project has been challenging. However, I'm committed to documenting and analyzing each testing finding encountered during development, along with potential solutions. While the testing process may not be comprehensive, this section aims to provide insights into the testing journey, highlighting areas for improvement and future iterations.

### Speed Testing
To evaluate the performance of this project, speed testing was conducted using https://pagespeed.web.dev/. This tool offers insights into the loading speed and optimization of web pages, helping to identify areas for improvement and enhance user experience.

The speed testing was done in the three main pages with big images as content:

**Index page:**
Based on the performance analysis, the index page achieved a performance score of 61, with accessibility and best practices scoring 91 and 100 respectively. While the SEO score reached 91, there's still room for enhancement across all metrics, particularly in performance. According to site speed analytics, the primary areas for improvement lie in optimizing image delivery and reducing layout shifting on the front page. This can be addressed by adjusting the loading type of certain content to lazy loading and implementing caching mechanisms for the hero image data, thereby enhancing overall page performance and user experience.

![](https://raw.githubusercontent.com/jhoanTrujillo/e-commerce-pp5/main/github_media/performance_main_page.png)

**Collection page:**
On the collection page, the performance score stands at 65, with accessibility at 96, best practices at 100, and SEO at 91. Analysis suggests that unused code, particularly in JavaScript, is contributing to performance issues. Additionally, the presence of unused elements from the Bulma library appears to be a significant factor in the page slowdown, closely followed by image optimization. To address this, considering a more lightweight version of Bulma could lead to overall speed improvements and better page performance.

![](https://raw.githubusercontent.com/jhoanTrujillo/e-commerce-pp5/main/github_media/collection_page_speed.png)
![](https://raw.githubusercontent.com/jhoanTrujillo/e-commerce-pp5/main/github_media/collection_page_speed_insight.png)
**Product page:**


![](https://raw.githubusercontent.com/jhoanTrujillo/e-commerce-pp5/main/github_media/mobile_product_page.png)
![](https://raw.githubusercontent.com/jhoanTrujillo/e-commerce-pp5/main/github_media/mobile_product_page_errors.png)

### Manual testing

### Python linter
This is just a general demonstration and of the 3 major apps and the py code there.

**Product app**
The majority of the issues in the view for the product app was based around indentation because the code had mixed indentation between tabs
and spaces. Other issues highlighted was the lines were too long. that was remediated by cutting some lines.
**Admin.py**
![](https://raw.githubusercontent.com/jhoanTrujillo/e-commerce-pp5/main/github_media/products_admin_py.png)
**Views.py**
![](https://raw.githubusercontent.com/jhoanTrujillo/e-commerce-pp5/main/github_media/products_views_py.png)
**models.py**
![](https://raw.githubusercontent.com/jhoanTrujillo/e-commerce-pp5/main/github_media/products_models_py.png)
**widgets.py**
![](https://raw.githubusercontent.com/jhoanTrujillo/e-commerce-pp5/main/github_media/products_widgets_py.png)
**forms.py**
![](https://raw.githubusercontent.com/jhoanTrujillo/e-commerce-pp5/main/github_media/products_forms_py.png)

**Home**
The home app had several linting errors related to the indentation. I noticed that the main thing I missed was the long strings not breaking in the right place and the spaces between functions. A interesting one was the last line needing a blank space which I missed almost 100% of the times. 

**Admin.py**
![](https://raw.githubusercontent.com/jhoanTrujillo/e-commerce-pp5/main/github_media/home_admin_py.png)
**Views.py**
![](https://raw.githubusercontent.com/jhoanTrujillo/e-commerce-pp5/main/github_media/home_views_py.png)
**models.py**
![](https://raw.githubusercontent.com/jhoanTrujillo/e-commerce-pp5/main/github_media/home_models_py.png)
**urls.py**
![](https://raw.githubusercontent.com/jhoanTrujillo/e-commerce-pp5/main/github_media/home_urls_py.png)
**forms.py**
![](https://raw.githubusercontent.com/jhoanTrujillo/e-commerce-pp5/main/github_media/home_forms_py.png)

**Checkout**
In the case of the checkout app I noticed that there was a bit less to worry about. As the app was made almost at the end with a bit more warmup there was a bit more care in the syntax and the usage of indentation. Not major issues other than a couple of long strings that needed to be cut down.

**Admin.py**
![](https://raw.githubusercontent.com/jhoanTrujillo/e-commerce-pp5/main/github_media/checkout_admin_py.png)
**Views.py**
![](https://raw.githubusercontent.com/jhoanTrujillo/e-commerce-pp5/main/github_media/checkout_views_py.png)
**models.py**
![](https://raw.githubusercontent.com/jhoanTrujillo/e-commerce-pp5/main/github_media/checkout_models_py.png)
**urls.py**
![](https://raw.githubusercontent.com/jhoanTrujillo/e-commerce-pp5/main/github_media/checkout_urls_py.png)
**forms.py**
![](https://raw.githubusercontent.com/jhoanTrujillo/e-commerce-pp5/main/github_media/checkout_forms_py.png)
**Signals**

### Bugs
Although there are some bugs documented in the project board I thought to bring to light some major or at least the most notable bugs I found here. 

**Major Bug: product image update**
- When updating products on the site using the super user account, users encounter difficulties uploading images directly into the S3 bucket.
The issue arises from problems with the required signature for submitting objects as PUT requests.

**Fallback Solution:**
- As a workaround, users can add the image URL instead of directly uploading images, enabling products to display images effectively.
This workaround applies to both products and variants.

**Ongoing Investigation:**
- Efforts are underway to determine the necessary steps to ensure AWS allows PUT access to the project.

---

**Major Bug: email confirmation**
- Confirmation emails are not being sent when orders are completed, resulting in a 500 page error.

**Fallback Solution:**
- Despite the email failure, user accounts are still being created, ensuring access to previous orders via the user profile.

**Ongoing Investigation:**
- Possible cause: Last-minute changes to the confirmation template may have altered the template inheritance, leading to email sending failures.

---

**Major Bug: Order email**
- When an order is completed, emails containing confirmation details are not being sent, resulting in customers not receiving order confirmations.

**Fallback Solution:**
- Users experiencing this issue can sign in to their accounts to access previous orders via the user profile, which tracks order history.

**Ongoing Investigation:**
- The erratic behavior of message windows may be attributed to conflicts between the message-box class code and the code handling forms on the page. Refreshing the page could serve as a temporary workaround until a permanent fix is implemented.

## Credits

### Resources used:
**CODE**
- [BULMA CSS](https://bulma.io/) - one of the main tools I used. Bulma provided the backbone of the project. The colors, fonts, and other design choices are handling automatically by the framework. 
- [Mailchimp newsletter box](https://mailchimp.com/help/add-a-signup-form-to-your-website/) - mailchimp docs have a embed for newsletter signatures that we use in our footer.

**Content**
- [Midjourney](https://www.midjourney.com/explore?tab=random) - image generation
- [Ubersuggest](https://www.midjourney.com/explore?tab=random) - keyword research
- [CHAT GPT](https://www.midjourney.com/explore?tab=random) - for product description using keywords
- [XML SITEMAPS](https://www.xml-sitemaps.com/) - for creating a sitemap

**Hosting and deployment**

- [Heroku](https://www.heroku.com/) - For deployment and hosting of site
- [Mailchimp](https://mailchimp.com/) - Mailchimp for newsletter handling
- [ElephantSQL](https://www.elephantsql.com/) - ElephantSQL for database
- [Stripe](https://dashboard.stripe.com/) - Stripe for payment processing
- [GMAIL](https://mail.google.com/) - used for email submission
- [Canva](https://www.canva.com/) - For creation of custom images and facebook page images
