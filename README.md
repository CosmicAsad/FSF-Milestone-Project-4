# Soundwaves

![Various Devices](https://github.com/CosmicAsad/FSF-Milestone-Project-4/blob/master/media/responsive-ms4_50.png)


---
Soundwaves is a website dedicated to music, and allows users to purchase a variety of CDs and vinyl records. The focus of the website is to allow people to view and purchase music as physical media, which offers unparalleled sound quality and allows fans to build their music collections. Various genres of music are listed, and Limited Edition copies are also available for purchase.

## NOTE: This project is for learning purposes only. The store does not exist, and as such there are no products being sold. There is no promotion taking place. All albums and their respective artworks belong to their respective owners.

---

## User Experience (UX)

---
### User Stories

**Viewing products & site navigation**

| User Story ID | User Type | What they want to achieve | End goal |
|:----------:|:-----------:|:----------:|:-----------:|
| 1.| Shopper | As a shopper, I want to view a selection of CDs and vinyls| So I can choose what to purchase. |
| 2.| Shopper | As a shopper, I want to view specific categories| So I can choose and filter products that interest me. |
| 3.| Shopper | As a shopper, I want to view the details of a product | So I can make a decision based on price, image, description, and reviews. |
| 4.| Shopper | As a shopper, I want to view the total price of the products I have added to my cart| So I can keep track of what I plan to purchase and avoid overspending. |
| 5.| Shopper | As a shopper, I want to search products using keywords| So I can quickly and easily find what I am looking for. |
| 6.| Shopper | As a shopper, I would like to sort through products by price, name, and genre | So I can compare products and choose based on my preferences. |
| 7.| Shopper | As a shopper, I want to view the items in my shopping cart | So I can view what I have chosen to purchase. |
| 8.| Shopper | As a shopper, I want to be able to review products | So I can leave recommendations for other users. |

**Registration and authentication**

| User Story ID | User Type | What they want to achieve | End goal |
|:----------:|:-----------:|:----------:|:-----------:|
| 1.| User | As a site user, I want to be able to create a new user account. | So I can access my new user profile. |
| 2.| User | As a site user, I want to be able to log into my existing account | So I can view my existing profile |
| 3.| User | As a site user, I want to view my order history in my profile | So I can keep track of what I have purchased. |
| 4.| User | As a site user, I want to save my details on checkout | So my next transaction is quicker by using my saved details. |
| 5.| User | As a site user, I want to edit my saved details | To keep them up to date for my next purchase. |
| 6.| User | As a site user, I would like my account to be secure with a password. | So no one else can brute force or access my account and take my details. |
| 7.| User | As a site user, I would like to be able to log out of my account | So I can end my session when I'm done shopping or viewing my profile. | 

**Admin and CRUD**

| User Story ID | User Type | What they want to achieve | End goal |
|:----------:|:-----------:|:----------:|:-----------:|
| 1.| Admin | As an admin, I want to be able to access product management. | So I can create, read, update, and delete products on the site. |
| 2.| Admin | As an admin, I want secure access to admin features | So non-superusers are unable to change update, or delete any products on the site. |
| 3.| Admin | As an admin, I want to be able to create new products | So I can add new products to the site once they are available for shoppers. |
| 4.| Admin | As an admin, I want to be able to read the data on each product | To check for errors and view the full information of each product uploaded to the site. |
| 5.| Admin | As an admin, I want to update existing products on my site | To fix errors, upload new images, and change product details when necessary. |
| 6.| Admin | As an admin, I would like the ability to delete items from the site | So they are unable to be purchased when they are no longer available for sale. |

**Purchasing and checkout**

| User Story ID | User Type | What they want to achieve | End goal |
|:----------:|:-----------:|:----------:|:-----------:|
| 1.| Shopper | As a shopper, I want to be able to add a product to my cart | So I can view a list of the products I intend to purchase |
| 2.| Shopper | As a shopper, I want the ability to choose the quantity of each item I add to the cart | So I can choose multiple of each item to purchase, or remove the item entirely. |
| 3.| Shopper | As a shopper, I want to view my cart on a separate page | So I can see the items i've chosen, the quantity, and the breakdown of the total and the delivery costs. |
| 4.| Shopper | As a shopper, I want the ability to check out the products | So I can add my delivery details and payment infotmation. |
| 5.| Shopper | As a shopper, I want the ability to securely submit my payment | So my order can be processed and my payment information is secure. |
| 6.| Shopper | As a shopper, I want the ability to save my details for next time | So I can checkout faster next time. |
| 7.| Shopper | As a shopper, I want to receive confirmation that my order was successful | So I can be certain that my order has been placed and my payment was successful. |
| 8.| Shopper | As a shopper, I want to receive an email confirmation that my order was successful | So I have an email that I can refer to for proof of the order. |

---

### UX Framework

**1. Strategy**

The design process of the website for Soundwaves was designed with the focus on primarily the customer, and the admin. The goal was to create a e-commerce website that utilised full-stack development to create a site that allows users to purchase music products, as well as allow creative control for myself as the admin. The website should provide a positive UX for the shoppers, as well as an easy to navigate UI. The goal of the project is to demonstrate my coding abilities using HTML, CSS, JavaScript, Python, as well as Django. The user stories detailed below provided additional strategy for what features to include.  

**2. Scope**

The scope of the project was to create a website that included must-have features for a fully functional e-commerce website, that allows shoppers to purchase CDs and vinyl records. The Boutique Ado project was followed for e-commerce aspects of the website. Additionally, some nice-to-have features were considered. These are detailed below.

**Functional Requirements**

Must-have features:
1. Site authentication for admin and shoppers. Users must be able to create an account to purchase products.
2. Site navigation. Functional links and searching are required for shoppers to easily view products and navigate the site.
3. The site must be responsive and work for users on various screen sizes and platforms.
4. Ability to view products and details.
5. Ability to add products to a cart.
6. A checkout page containing a user input form for a user to enter their details.
7. The site must provide the user with feedback in the event of errors and when taking certain actions.
8. The site must provide a order confirmation once the purchase is successful.
9. A user profile must allow users to register a new account and log in to existing accounts.
10. The profile page must let the user view their orders and save their delivery information.
11. The Admin/Superuser must have CRUD functionality available.
12. CRUD functionality should be restricted for normal users.

To test the Stripe payment function please use the following details:
**Card Number**: 4242 4242 4242 4242
**Expiration Date**: 04/24
**CVC number**: 242
**Zip code**: 42424

Nice to have features:
1. Advanced search filter for genre,
2. A "recommended for you" section to provide existing users with new products to order.
3. Inventory count for each product.
4. Additional images showing the back of each album.
5. The track-listing for each album.

Additional features such as complete social media integration, as well as stock updates via email were considered as part of the design process, but were ultimately discarded due to time constraints.

**Content Requirements**
1. A mixed list of products so there is at least an item in each category.
2. A products page with clear images and information about each album.
3. The price of each item.
4. A visual aid showing the current total of products in the cart.
5. Product details including a short description, name, artist, image, and price of each album.
6. Toasts that respond to events such as adding a product and checking out.

**3. Structure**

The structure of the website follows the same basic structure laid out in the Boutique Ado project.
*The home page consists of the header, site navigation, a splash image, and a footer.
*The header contains the site name and logo, the search bar, links for the account page and cart, and the navbar. Lof in and register links are provided to users that are not in an active session.
*The log in page allows an existing user to access their account via a form for username and password. Once authenticated the user is redirected to their profile page.
*The register page allows a new user to create a new account. Once completed the user is redirected to their profile page.
*The profile page stores the users details such as address and order history. This allows users to check out faster.
*The navbar contains links for 'All Products', CDs, Vinyls, and Limited Editions. Each of these open a dropdown menu for various categories to allow shoppers to filter items.
*Each category page follows the same structure of a grid of products, and each product card has an image (if available), a name, artist, price, and genre.
*Individual products can be selected to open the product details page. This provides a larger image of the item, a description, as well as the information from the previous page.
*The product details page allows the user to add the item to their shopping cart via the 'Add to cart' button.
*Once added, the displayed total will be updated to show the current total price of the items in the cart.
*The checkout page can be accessed via the cart icon and consists of a form, which allows the user to enter their details and purchase the item.
*Once the purchase is complete, the order details are provided and a link allows the user to continue shopping.
*An email confirmation containing the order details is sent to the user.

**4. Skeleton**
The skeleton of the site was created using Balsamiq wireframes. A wireframe was constructed utilising the scope and structure aspects of the UX framework to create a design for a functional website that is consistent with my strategy. This provided a template for the final website design.
This also allowed me to consider the responsive design and how elements of the site interacted with each other on large screen sizes as well as mobile.
This provided a useful plan going into the site construction and allowed me to visualise the final website design.

### Wireframe

[Wireframe PDF made in Balsamiq](https://github.com/CosmicAsad/FSF-Milestone-Project-4/blob/master/static/wireframes/MS4-wireframe.pdf)

**5. Surface**

*The surface of the website aims to appeal to a range of users with a sleek and professional design, with a layout that is familiar to users. This was achieved by following current design methods to provide a satisfactory user experience for visitors, which prevents frustration from unfamiliar design.
*As the website is a store for CDs and vinyl records, the home page consists of a striking background image of a vinyl record and minimal overlaying text. This was chosen to make it apparent to the user that the focus of the site is music products.
*An easily legible font was chosen throughout the site; Montserrat. This was obtained from Google fonts and provides a modern and interesting typeface for users whilst also being easy to read and in line with the music/technology theme of the website.
*The header uses the Montserrat font and the text colour used is white, to provide contrast against the darker background.
*The products page consists of a grid layout of the individual products arranged in order (as specified by the shopper).
*Each product Has a displayed image, as well as the name, artist, price and genre below it, to be clearly visible to the shopper.

The colours used were chosen using HTML color picker and are as follows:

* #008080
* #029bab
* #000000
* #ffffff
* #aab7c4

The images consist of the album artwork for each CD and Vinyl to be instantly recognisable to music fans. The sources are listed below in the Media category.

## Features

### Existing Features

1. Django Allauth
2. Site navigation
3. Styling
4. Stripe
5. Amazon Web Services to host static and media files
6. Fully customised home page
7. User profile page
8. Login page
9. Register page
10. Product details
11. Product management for admin - CRUD
12. Sorting and filtering
13. Emails for checkout success
14. User email verification
15. Webhooks
16. Fully responsive design
17. Deployed site on Heroku

### Upcoming Features

1. Product reviews
2. Wishlist

## Technologies Used

 - HTML: Used to create the structure and the content of the website.
 - CSS: Used to style the webpage and provide an appealing design for users.
 - JavaScript: Used for backend functionality and logic of various functions throughout the site.
 - Python: Used to create the main backend logic of the website.
 - Django: Framework used for site functionality based on Python.
 - Bootstrap: Used to provide a starter template and aid responsiveness with various built-in classes.
 - Heroku: Used to deploy the site and make it visible.
 - Amazon Web Services (AWS): Used to host static and media files for the deployed website.
 - Balsamiq: Used to create my wireframe.
 - Gitpod: The IDE used to develop this project was gitpod.
 - Chrome Developer Tools: Used for debugging, checking responsiveness, and testing.

## Testing

**User Story Testing**

**Viewing products & site navigation**

| User Story ID | User Type | What they want to achieve | End goal | Testing |
|:----------:|:-----------:|:----------:|:-----------:|:-----------:|
| 1.| Shopper | As a shopper, I want to view a selection of CDs and vinyls| So I can choose what to purchase. | Search functionality using artist name and product name, and product viewing via the navigation options is fully available. |
| 2.| Shopper | As a shopper, I want to view specific categories| So I can choose and filter products that interest me. | Specific categories can be chosen via the navbar dropdown, and the sort options on each products subcategory. |
| 3.| Shopper | As a shopper, I want to view the details of a product | So I can make a decision based on price, image, description, and reviews. | Product details can be viewed by clicking on a product, showing all it's information. Basic information is shown in the products page. |
| 4.| Shopper | As a shopper, I want to view the total price of the products I have added to my cart| So I can keep track of what I plan to purchase and avoid overspending. | The cart provides a running total of the products added by the shopper, and will increase if products are added, and decrease if products are removed via the quantity selector |
| 5.| Shopper | As a shopper, I want to search products using keywords| So I can quickly and easily find what I am looking for. | Products can be searched via the search form, using the artist name, and album name |
| 6.| Shopper | As a shopper, I would like to sort through products by price, name, and genre | So I can compare products and choose based on my preferences. | Product sorting can be done via the sort selector oon the products page for each subcategory, allowing them to be sorted alphabetically by name, genre, and artist, as well as price. Ascending and descending options are available for each. |
| 7.| Shopper | As a shopper, I want to view the items in my shopping cart | So I can view what I have chosen to purchase. | The shopping cart can be viewed by clicking the cart icon in the top right of the header, showing a running total and product details of items added to the cart, as well as calculated delivery costs. |
| 8.| Shopper | As a shopper, I want to be able to review products | So I can leave recommendations for other users. | The review form can be found on the product detail page and allows users to submit a review. |


**Registration and authentication**

| User Story ID | User Type | What they want to achieve | End goal | Testing |
|:----------:|:-----------:|:----------:|:-----------:|:-----------:|
| 1.| User | As a site user, I want to be able to create a new user account. | So I can access my new user profile. | A new user account can be created by clicking the profile icon in the top right, and clicking register. A form can be filled out with user details including email, username, and password. A verification email is sent once submmitted, and a user must be verified to access their profile. |
| 2.| User | As a site user, I want to be able to log into my existing account | So I can view my existing profile | Existing users can log in via the profile icon in the top right and clicking Login. The user can fill in their login credentials to access their profile. |
| 3.| User | As a site user, I want to view my order history in my profile | So I can keep track of what I have purchased. | The user profile shows the order history associated with the linked user, and provides the order number, total, date, and items. |
| 4.| User | As a site user, I want to save my details on checkout | So my next transaction is quicker by using my saved details. | Details are saved on checkout if the user selects the corresponding box to save details. This is only available to authenticated users. |
| 5.| User | As a site user, I want to edit my saved details | To keep them up to date for my next purchase. | Saved details can be edited and updated by the user in the user profile. These will prefill the form the next time the user checks out. |
| 6.| User | As a site user, I would like my account to be secure with a password. | So no one else can brute force or access my account and take my details. | Account is secured with django allauth and email verification is required for access for new users. Passwords are hidden. |
| 7.| User | As a site user, I would like to be able to log out of my account | So I can end my session when I'm done shopping or viewing my profile. | Log out is available via the profile icon once logged in, and allows user to confirm they want to sign out |

**Admin and CRUD**

| User Story ID | User Type | What they want to achieve | End goal | Testing |
|:----------:|:-----------:|:----------:|:-----------:|:-----------:|
| 1.| Admin | As an admin, I want to be able to access product management. | So I can create, read, update, and delete products on the site. | Product management is available only when logged in as the admin/superuser from the profile icon on the top right. |
| 2.| Admin | As an admin, I want secure access to admin features | So non-superusers are unable to change update, or delete any products on the site. | Non superusers are returned to the homepage if trying to access any CRUD functions, and cannot access product management. |
| 3.| Admin | As an admin, I want to be able to create new products | So I can add new products to the site once they are available for shoppers. | New products can be created using the product management link. |
| 4.| Admin | As an admin, I want to be able to read the data on each product | To check for errors and view the full information of each product uploaded to the site. | All users have the functionality to view the product data. Admins can log in to the django portal to view additional data like product codes. |
| 5.| Admin | As an admin, I want to update existing products on my site | To fix errors, upload new images, and change product details when necessary. | Edit products is available and funvtional for the admin from each product card on the products page, allowing details to be updated. |
| 6.| Admin | As an admin, I would like the ability to delete items from the site | So they are unable to be purchased when they are no longer available for sale. | Deleting items is available from the products card as well, and is able to remove the product. |

**Purchasing and checkout**

| User Story ID | User Type | What they want to achieve | End goal | Testing |
|:----------:|:-----------:|:----------:|:-----------:|:-----------:|
| 1.| Shopper | As a shopper, I want to be able to add a product to my cart | So I can view a list of the products I intend to purchase. | Products can be added to the cart from the product detail page via the add to cart button. |
| 2.| Shopper | As a shopper, I want the ability to choose the quantity of each item I add to the cart | So I can choose multiple of each item to purchase, or remove the item entirely. | The quantity can be selected with a minimum of 1 or maximum of 99 of each item using the quantity selector on the product details page. |
| 3.| Shopper | As a shopper, I want to view my cart on a separate page | So I can see the items i've chosen, the quantity, and the breakdown of the total and the delivery costs. | The cart can be viewed by clicking the cart icon on the top left, which shows the current cart contents on a separate page. |
| 4.| Shopper | As a shopper, I want the ability to check out the products | So I can add my delivery details and payment infotmation. | Products can be checked out by clicking the checkout form on the cart page, and filling in delivery details and payment information. |
| 5.| Shopper | As a shopper, I want the ability to securely submit my payment | So my order can be processed and my payment information is secure. | Payment is handled by filling out the test payment information (4242 4242 4242 4242 04/24 42424) and submitting. If payment is succesful a confirmation will be displayed via a toast and success page. |
| 6.| Shopper | As a shopper, I want the ability to save my details for next time | So I can checkout faster next time. |A checkbox below the details form allows users to save their delivery details for next time. These are confirmed to show up on user's the profile page. |
| 7.| Shopper | As a shopper, I want to receive confirmation that my order was successful | So I can be certain that my order has been placed and my payment was successful. | A success page and toast confirming the order number and details will be displayed upon successful checkout. |
| 8.| Shopper | As a shopper, I want to receive an email confirmation that my order was successful | So I have an email that I can refer to for proof of the order. | An email is sent upon successful checkout to the user's email address provided during checkout. |

**Validation testing**

All CSS and JavaScript files have been checked using the W3 validator, with only an error regarding language declaration for each file, which I have chosen to ignore.

## Deployment

### Heroku Deployment

### AWS Setup

1. To set up AWS, first [create an AWS account](https://aws.amazon.com/free/)
2. Create an S3 bucket and a bucket policy.
3. Create a user group, an access policy for your users, and finally users. 
--- These steps are detailed in [Getting Started with Amazon S3](https://aws.amazon.com/s3/getting-started/) ---
4. Connect Django to the S3 bucket using S3Boto3Storage and following Django storage setup steps at the doc found [here](https://django-storages.readthedocs.io/en/1.11.1/backends/amazon-S3.html)
5. Set Heroku config vars for AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY using keys obtained from S3 user setup.
6. Set USE_AWS to True in Heroku config vars.

## Credits

### Content

Content was created by following the steps laid out in the Code Institute Boutique Ado project. I have tried to customise the code as much as possible for my own use case whilst following these steps. No other sources were used for the site. Therefore a majority of the code used for the models can be attributed to the Boutique Ado source code, with the exception of the custom Django models.

### Media

---

**Images**

Homepage image:

The main homepage image used on the site is a free stock image taken from Pexels https://www.pexels.com/photo/blue-vinyl-record-playing-on-turntable-1389429/

---

#### NOTE: This project is for learning purposes only. The store does not exist, and as such there are no products being sold. There is no promotion taking place. All albums and their respective artworks belong to their respective owners.

A list of sources used to provide images for the album covers for the Pop CDs featured on the site:

1. [Ed Sheeran - Divide](https://www.amazon.co.uk/%C3%B7-Divide-Ed-Sheeran/dp/B01MY72DBS?ref_=Oct_s9_apbd_oup_hd_bw_b2uau&)
2. [Taylor Swift - Evermore](https://www.amazon.co.uk/Evermore-album-deluxe-Taylor-Swift/dp/B08Q9MLYPQ/ref=sr_1_22?dchild=1&)
3. [Little Mix - Confetti](https://www.amazon.co.uk/Confetti-Little-Mix/dp/B08JB9RRR8/ref=sr_1_19?dchild=1&)
4. [Ariana Grande - Positions](https://www.amazon.co.uk/Positions-Ariana-Grande/dp/B08L41BDBP/ref=sr_1_2?crid=1XLFUOVNKNOFC&dchild=1&keywords=ariana+grande+cd&qid=1621346994&s=music&sprefix=ari%2Cpopular%2C184&sr=1-2)
5. [Justin Bieber - Justice](https://www.amazon.co.uk/Justice-Justin-Bieber/dp/B08X6C6Z2G/ref=sr_1_45?dchild=1&qid=1621347121&refinements=p_n_binding_browse-bin%3A382528011&rnid=382527011&s=music&sr=1-45)
6. [Dua Lipa - Dua Lipa (Complete Edition)](https://www.amazon.co.uk/Dua-Lipa-Complete/dp/B07J33Q54P/ref=sr_1_4?crid=3KYDHFLUR28W1&dchild=1&keywords=dua+lipa+cd&qid=1621347313&s=music&sprefix=dua+%2Cpopular%2C177&sr=1-4)
7. [Sam Smith - Love Goes](https://www.amazon.co.uk/Love-Goes-Sam-Smith/dp/B08FTKJ4GF/ref=sr_1_1?crid=9ST2XABC9RC9&dchild=1&)
8. [Miley Cyrus - Plastic Hearts](https://www.amazon.co.uk/Plastic-Hearts-Miley-Cyrus/dp/B08LN979N2/ref=sr_1_67?dchild=1&qid=1621348050&s=music&sr=1-67)
9. [Coldplay - Everyday Life](https://www.amazon.co.uk/Everyday-Life-Coldplay/dp/B07YMDZZW8/ref=sr_1_96?dchild=1&qid=1621348134&s=music&sr=1-96)
10. [Black Eyed Peas - Translation](https://www.amazon.co.uk/Translation-Black-Eyed-Peas/dp/B088K718T8/ref=sr_1_1?crid=1XC267VNM53N1&dchild=1&)

---
A list of sources used to provide images for the album covers for the Hip-hop CDs featured on the site:

1. [Madvillain - Madvillainy](https://www.amazon.co.uk/Madvillainy-Madvillain/dp/B00018Y0QQ/ref=sr_1_1?dchild=1&keywords=madvillainy&qid=1621349134&s=music&sr=1-1)
2. [Juice WRLD - Legends Never Die](https://www.amazon.co.uk/Legends-Never-Die-Juice-WRLD/dp/B08H5BLFBT/ref=sr_1_1?dchild=1&keywords=juice+wrld&qid=1621349199&s=music&sr=1-1)
3. [Pop Smoke - Shoot For The Stars Aim For The Moon](https://www.amazon.co.uk/Shoot-Stars-Aim-Moon-Smoke/dp/B08CWCG1V3/ref=sr_1_1?dchild=1&keywords=pop+smoke&qid=1621349246&s=music&sr=1-1)
4. [Drake - Scorpion](https://www.amazon.co.uk/Scorpion-Drake/dp/B07F464TC8/ref=sr_1_4?dchild=1&keywords=drake&qid=1621349398&s=music&sr=1-4)
5. [Notorious B.I.G. - Greatest Hits](https://www.amazon.co.uk/Greatest-Hits-Notorious-B-I-G/dp/B000NA25P0/ref=tmm_acd_swatch_0?_encoding=UTF8&qid=1621349447&sr=1-1)
6. [Travis Scott - Astroworld](https://www.amazon.co.uk/Astroworld-Travis-Scott/dp/B07FYQR5QQ/ref=sr_1_3?crid=24YUQ8BDGNSUH&dchild=1&keywords=travis+scott+cd&qid=1621349707&s=music&sprefix=travis+s%2Cpopular%2C197&sr=1-3)
7. [J Cole - 2014 Forest Hills Drive](https://www.amazon.co.uk/2014-Forest-Hills-Drive-Cole/dp/B00POE9JV8/ref=tmm_acd_swatch_0?_encoding=UTF8&qid=1621349799&sr=1-3)
8. [Stormzy - Heavy Is The Head](https://www.amazon.co.uk/Heavy-Head-Stormzy/dp/B081KRT169/ref=sr_1_1?crid=2U9LI0UCB0OND&dchild=1&keywords=stormzy&qid=1621349972&s=music&sprefix=Storm%2Cpopular%2C195&sr=1-1)
9. [Eminem - Kamikaze](https://www.amazon.co.uk/Kamikaze-Eminem/dp/B07GZTDDMW/ref=pd_sim_44/261-4749870-1301622?pd_rd_w=JaXBg&)
10. [Jay-Z - The Blueprint](https://www.amazon.co.uk/Blueprint-JAY-Z/dp/B00005O54T/ref=pd_sim_37/261-4749870-1301622?pd_rd_w=jPsfW&)

---
A list of sources used to provide images for the album covers for the Rock CDs featured on the site:

1. [Linkin Park - Hybrid Theory](https://www.amazon.co.uk/Hybrid-Theory-Linkin-Park/dp/B00004Z459/ref=sr_1_8?crid=1ROTVJ0J51QZG&dchild=1&)
2. [My Chemical Romance - The Black Parade](https://www.amazon.co.uk/Black-Parade-My-Chemical-Romance/dp/B000I5Y8ZU/ref=sr_1_1?crid=1SVAQ97XZWSWN&dchild=1&keywords=my+chemical+romance+cd&qid=1621352513&s=music&sprefix=my+che%2Cpopular%2C186&sr=1-1)
3. [All Time Low - Wake Up, Sunshine](https://www.amazon.co.uk/Wake-Sunshine-Amazon-Exclusive-Signed/dp/B084QL471J/ref=sr_1_3?dchild=1&)
4. [The All-American Rejects - When The World Comes Down](https://www.amazon.co.uk/When-World-Comes-American-Rejects/dp/B001N2UXUG/ref=sr_1_3?crid=1YZ7NIH1I0DVZ&dchild=1&keywords=all+american+rejects&qid=1621354478&s=music&sprefix=all+amer%2Cpopular%2C172&sr=1-3)
5. [Arctic Monkeys - AM](https://www.amazon.co.uk/AM-Arctic-Monkeys/dp/B00DYFCTSY/ref=sr_1_2?keywords=arctic+monkeys&qid=1621354657&s=music&sr=1-2)
6. [Bring Me The Horizon - Sempiternal](https://www.amazon.co.uk/Sempiternal-Bring-Me-Horizon/dp/B00C57DFY4/ref=sr_1_5?crid=21SW1AKMJ33IO&dchild=1&keywords=bring+me+the+horizon&qid=1621355781&s=music&sprefix=bring+me%2Cpopular%2C187&sr=1-5)
7. [The Amazons - Future Dust](https://www.amazon.co.uk/Future-Dust-Amazons/dp/B07Q2JHJNN/ref=sr_1_4?crid=BRIJKFPWFRLA&keywords=the+amazons&qid=1621355902&s=music&sprefix=the+amaz%2Cpopular%2C162&sr=1-4)
8. [Fall Out Boy - Mania](https://www.amazon.co.uk/Fall-Out-Boy-Mania-PL/dp/B0796Y8LDP/ref=sr_1_3?crid=3P9EE65RPSFS0&dchild=1&keywords=fallout+boy+cd&qid=1621356134&s=music&sprefix=fal%2Cpopular%2C196&sr=1-3)

---
A list of sources used to provide images for the album covers for the Pop vinyls featured on the site:

1. [The Killers - Hot Fuss](https://www.amazon.co.uk/Killers-Exclusive-Transparentes-Orange-NM-Zustand/dp/B07PPXRKJQ/ref=sr_1_9?)
2. [Adele -25](https://www.amazon.co.uk/25-VINYL-Adele/dp/B0170C28BE/ref=sr_1_10?dchild=1&)
3. [Amy Winehouse -  Back to Black](https://www.amazon.co.uk/Back-Black-VINYL-Amy-Winehouse/dp/B000P5FG1I?ref_=Oct_s9_apbd_omwf_hd_bw_b2)
4. [The Weeknd - Starboy](https://www.amazon.co.uk/Starboy-Weeknd/dp/B01LTHY0H6/ref=sr_1_3?dchild=1&keywords=weeknd&qid=1621273636&s=music&sr=1-3)
5. [The Weeknd - After Hours](https://www.amazon.co.uk/After-Hours-VINYL-Weeknd/dp/B084XTMZVS/ref=sr_1_2?dchild=1&keywords=weeknd&qid=1621273689&s=music&sr=1-2)
6. [Taylor Swift - 1989](https://www.amazon.co.uk/1989-VINYL-Taylor-Swift/dp/B00PA04SD0/ref=sr_1_2?dchild=1&keywords=taylor+swift+vinyl&qid=1621273762&s=music&sr=1-2)
7. [Harry Styles - Fine Line](https://www.amazon.co.uk/Fine-Line-VINYL-Harry-Styles/dp/B07ZWBNZR4/ref=sr_1_21?dchild=1&qid=1621273995&s=music&sr=1-21)
8. [Paul Weller - Fat Pop](https://www.amazon.co.uk/Fat-Pop-VINYL-Paul-Weller/dp/B08WZJK2X2/ref=sr_1_17?dchild=1&qid=1621273995&s=music&sr=1-17)
9. [Louis Tomlinson - Walls](https://www.amazon.co.uk/Walls-VINYL-Louis-Tomlinson/dp/B07Z74SSBP/ref=sr_1_31?dchild=1&qid=1621274260&s=music&sr=1-31)
10. [Billie Eilish - Happier Than Ever](https://www.amazon.co.uk/Happier-Than-Ever-Billie-Eilish/dp/B093KVZNHX/ref=sr_1_40?dchild=1&qid=1621274353&s=music&sr=1-40)

---
A list of sources used to provide images for the album covers for the Hip-hop vinyls featured on the site:

1. [Czarface & MF DOOM - Super What?](https://www.normanrecords.com/records/187220-czarface-mf-doom-super-what?gclid=CjwKCAjwqIiFBhAHEiwANg9szj5pB87rhoLrW1_91fxZHlZg537kRpZVnWPViFTUh__MUwZ5CBHQTRoCf7AQAvD_BwE)
2. [2Pac - All Eyez on Me](https://www.amazon.co.uk/All-Eyez-Explicit-Version-VINYL/dp/B00005AQE7)
3. [Nas - Illmatic](https://www.amazon.co.uk/Illmatic-Clean-Version-VINYL-Nas/dp/B00004WX4X/ref=sr_1_9?dchild=1&keywords=illmatic&qid=1621270695&s=music&sr=1-9)
4. [Kendrick Lamar - Good Kid mAAd City](https://www.amazon.co.uk/good-kid-m-city-VINYL/dp/B009F1ZYO2/ref=sr_1_1?crid=2MMGDXU8T2BY4&dchild=1&keywords=good+kid+maad+city+vinyl&qid=1621270730&s=music&sprefix=good+kid%2Cpopular%2C189&sr=1-1)
5. [Eminem - Curtain Call](https://www.amazon.co.uk/Curtain-Call-VINYL-Eminem/dp/B000BYRD6Y/ref=sr_1_1?crid=1P6WFSS2QQNK0&dchild=1&keywords=curtain+call&qid=1621272088&s=music&sprefix=curta%2Cpopular%2C195&sr=1-1)
6. [NWA - Straight Outta Compton](https://www.amazon.co.uk/Straight-Outta-Compton-Anniversary-VINYL/dp/B000XCZGPE/ref=sr_1_10?dchild=1&keywords=nwa+vinyl&qid=1621272044&rnid=229816&s=music&sr=1-10)
7. [Ice Cube - The Greatest Hits](https://www.amazon.co.uk/Greatest-Hits-VINYL-Ice-Cube/dp/B00005S6VM/ref=sr_1_1?crid=101CHICW0ZVT1&dchild=1&keywords=ice+cube+greatest+hits+vinyl&qid=1621272124&sprefix=ice+cube+greatest+hits+%2Cpopular%2C219&sr=8-1)
8. [The Game - The Documentary](https://www.amazon.co.uk/Documentary-VINYL-Game/dp/B00PIFMKMS/ref=sr_1_1?crid=QC63JYENC6N&dchild=1&keywords=the+game+documentary+vinyl&qid=1621272163&sprefix=the+game+documen%2Caps%2C201&sr=8-1)
9. [50 Cent - Curtis](https://www.amazon.co.uk/Curtis-VINYL-50-Cent/dp/B000UZ4VB4/ref=sr_1_5?crid=1PIURBMIF4502&dchild=1&keywords=50+cent+vinyl&qid=1621272601&sprefix=50+cent%2Caps%2C219&sr=8-5)

---
A list of sources used to provide images for the album covers for the Rock vinyls featured on the site:

1. [Green Day - American Idiot](https://www.amazon.co.uk/American-Idiot-VINYL-Green-Day/dp/B00061Q83Q/ref=sr_1_3?dchild=1)
2. [Oasis - (What's The Story) Morning Glory?](https://www.amazon.co.uk/Whats-Story-Morning-Glory-VINYL/dp/B00LCT48L0/ref=sr_1_11?dchild=1&keywords=oasis&qid=1621275032&s=music&sr=1-11)
3. [Royal Blood - Typhoons](https://www.amazon.co.uk/Typhoons-VINYL-Royal-Blood/dp/B08SNN3XM1/ref=tmm_vnl_swatch_0?_encoding=UTF8&qid=1621275158&sr=1-1)
4. [Imagine Dragons - Night Visions](https://www.amazon.co.uk/Night-Visions-VINYL-Imagine-Dragons/dp/B008XOXGL0/ref=sr_1_1?dchild=1&keywords=imagine+dragons+vinyl&qid=1621275314&s=music&sr=1-1)
5. [Weezer - Van Weezer](https://www.amazon.co.uk/Van-Weezer-VINYL/dp/B085RS9PQV/ref=sr_1_1?dchild=1&keywords=weezer+vinyl&qid=1621275394&s=music&sr=1-1)
6. [AC/DC - Back in Black](https://www.amazon.co.uk/Back-Black-Rmst-VINYL-Ac/dp/B0000CF35G/ref=sr_1_3?dchild=1&keywords=back+in+black+vinyl&qid=1621275466&s=music&sr=1-3)
7. [Metallica - Ride the Lightning](https://www.amazon.co.uk/Ride-Lightning-Gram-Vinyl-VINYL/dp/B01BUX7Z7Q/ref=sr_1_6?crid=1WXFQRVKJI7GH&dchild=1&keywords=metallica+vinyl&qid=1621275545&s=music&sprefix=metallica%2Cpopular%2C174&sr=1-6)
8. [Blink 182 - Greatest Hits](https://www.amazon.co.uk/Greatest-Hits-VINYL-Blink-182/dp/B01M8I070D/ref=sr_1_6?dchild=1&keywords=blink+182+vinyl&qid=1621275667&s=music&sr=1-6)
9. [The 1975 - The 1975](https://www.amazon.co.uk/1975-VINYL/dp/B00CLOH240/ref=sr_1_1?dchild=1&keywords=the+1975+vinyl&qid=1621275780&s=music&sr=1-1)
10. [Liam Gallagher - Why Me? Why Not.](https://www.amazon.co.uk/Why-Me-Not-VINYL/dp/B07SQNQ577/ref=sr_1_1?dchild=1&keywords=liam+gallagher+vinyl&qid=1621275860&s=music&sr=1-1)

---

A list of sources used to provide images for the album covers for the Rock vinyls featured on the site:

1. [Motorhead - Bad Magic (Limited Edition)](https://www.amazon.co.uk/Bad-Magic-Motorhead/dp/B00YPB10F4/ref=sr_1_1?dchild=1&keywords=motorhead+-+bad+magic&qid=1622219845&sr=8-1)
2. [BTS - BE (Deluxe Edition)](https://www.amazon.co.uk/BTS-DELUXE-ALBUM-Polaroid-Postcards/dp/B08NWVYQ12/ref=sr_1_6?crid=3F2OIIHEHROAH&dchild=1&keywords=bts+limited+edition&qid=1622220135&sprefix=bts+limi%2Caps%2C261&sr=8-6)
3. [Eminem - Music To Be Murdered By - Side B (Deluxe Edition)](https://www.amazon.co.uk/Music-Be-Murdered-Side-Deluxe/dp/B08R1HP27T/ref=sr_1_1?dchild=1&keywords=eminem+side+b+deluxe&qid=1622220256&sr=8-1)
4. [The Roling Stones - The Lost Chess Tapes (Limited Edition)](https://www.amazon.co.uk/Chess-Tapes-Limited-Vinyl-VINYL/dp/B01FSNIN6Q/ref=sr_1_1?dchild=1&keywords=lost+chess+tapes&qid=1622220395&sr=8-1)

---

- Google Fonts was used to obtain the font 'Montserrat' [Google Fonts Link](https://fonts.google.com/specimen/Montserrat)

- FontAwesome 5 was used to provide various icons used throughout the site. [FontAwesome](https://fontawesome.com/)

- Favicons were obtained using [favicon.io](https://favicon.io/)

- SimpleImageResizer tool was used to change the sizes of some album artworks that were inconsistently sized. [SimpleImageResizer](http://www.simpleimageresizer.com/)

- Am I Responsive? was used to generate the responsive design image at the top of this README file. [Am I Responsive?](http://ami.responsivedesign.is/)

### Acknowledgements

- Code Institute group on slack
- Tutor support team