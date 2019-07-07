# 4Orn
# Simple calculator with NN instead math functions

## Essence

Hi 

I had created a Neural Network Calculator with four functions:

- **Addition** — sum: +
- **Subtraction** — sub: –
- **Multiplication** — mul: ×
- **Division** — div: ÷

## About Calculator's idea

My calc has three persons in self:

- **Bash** — my friend
- **Ivan** — my friend and classmate
- **Alba** — my gf

A made NN for all of this people K-times, where K is number of operation type

Models have differences in **hidden_layer_size**:

- **Bash** — has *(5, )* numbers of hll
- **Ivan** — has *(10, )* numbers of hll
- **Alba** — has *(50, )* numbers of hll

And i was interested, what will be :)

## About project

There are three main folders:

- **data** — handmade data-file with four type of operations
- **func** — func-file with functions, which I made 
- **pickle** — pickle-file with object — list of trained models

### data-file

I made him by hand with Excel

### func

There are five fuctions in:

- **load_data** — load Excel-csv and separate it right. ~~Yeah!, csv from Excel need more preparation, than default~~
- **make_models** — make ~~nude~~ empty models
- **train_models** — train models ~~very long time~~
- **pickled** — can save or load .pickle file
- **get_answer** — final, get full information about result:
- - NN summary answer
- - True answer
- - List of differences between answers
- - ID of winner
- - Name of winner
- - Every person answers

### pickle

Just  folder to save trained models

## Screenshots!

### Start 

![start](https://raw.githubusercontent.com/andybeardness/4Orn_Neural_Network_Calculator/master/imgs/start.png)

### True answer

![true](https://raw.githubusercontent.com/andybeardness/4Orn_Neural_Network_Calculator/master/imgs/true.png)

### False answer

![false](https://raw.githubusercontent.com/andybeardness/4Orn_Neural_Network_Calculator/master/imgs/false.png)

### Error

![error](https://raw.githubusercontent.com/andybeardness/4Orn_Neural_Network_Calculator/master/imgs/error.png)

# Thanks for attention ^^


