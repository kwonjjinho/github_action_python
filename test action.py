name: Test Action
on: [push]

jobs:
  get-num-square:
    runs-on: ubuntu-latest
    name: return the number square
    steps:
      - name:Checkout
        uses" action/checkout@v2
      - name: fetch num squared
        id: get_square
        uses: ./
        
