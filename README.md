* # RECIPEAZE...

An interactive website for saving recipeeeessss eazy peazy...

## Database Design

### Tables

![Database Tables](images/design_db_tables.png?raw=true "DB Tables")

#### User

* Username (primary key)
* Password

#### Recipe

* ID (primary key)
* Name
* Ingredients (through link table)
* Tags (through link table)
* Steps ... this might need its own table...
* Comments (design tbd)
* Main image (link)
* Favourit / Rating

#### Ingredient

* ID (primary key)
* Name

#### Tag

* ID (primary key)
* Name

## Website Design

Overview of the pages used in the site

### enter.erb

* This page has the enter button, scope to add login screen
* Clicking enter sends you to the List page

![Enter Page](images/design_enter.png?raw=true "Enter Page")

### list.erb

* This page has the list of recipes (for the user).
* Each recipe is displayed by the title and clicking the title is a link to the view page for the recipe
* Each recipe has option to delete or edit the recipe
* A mini render of the recipe main image is diaplyed next to the image
* There is a link to Add Recipe that links to the Add / Update page

![List Page](images/design_list.png?raw=true "List Page")

### add.erb

* This page is the interface to add a new recipe
* There are inpus for Name, Ingredients with quantity, Method entry (with step image), add tags.
* The ingredients are picked from a list of existing ingredients with the option to add a new ingredient
* The tags are selectable from existing tags and new tags can be added through this page

![Add Page](images/design_add.png?raw=true "Add Page")

### view.erb

* This page is the displays the selected recipe
* The main image for the recipe will be diaplsyed
* The ingredient list with quantity will be diplayed
* The steps with step images will be displayed

![View Page](images/design_view.png?raw=true "View Page")

### Test

* Test comment for Git push/pull validation
