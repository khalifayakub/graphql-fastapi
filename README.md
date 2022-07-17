# GraphQL FAST API
## Description
This is a simple api implemented using fastapi and graphql. It uses products.json to import mock data.
With the help of the api, you can query product overview, products by category and product details by product id.

## RUNNING THE PROGRAM
### Download the project
Download the zip file and extract it. Please make sure you have python Installed. Thank you.
### Installing the dependencies
run `pip install -r requirements.txt`
### Running the program
run `uvicorn main:app --reload`

## Queries to use
### Getting product overview
`{
  productOverview {
    products {
      name,
      price,
      category
    },
  	totalProducts,
    totalPrice
  }
}`
### Getting product details
`
{
  productDetails(id: 1) {
    name,
    price,
    category
  }
}
`
### Getting products by category
{
  productsByCategory(id: 1) {
    name,
    price,
    category
  }
}
