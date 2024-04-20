# Exercises for Class 8

The following are some exercises after class 8 (2024-04-18).

You should notice that there is some code already written,
you just need to add/update the code near "FIXME".

---

## Exercise 1


There is starter code in `ex-8-voltage.py`.


There is a bunch of data from 4 sensors.
(They are named; front, back, right, left.)

One of the sensors is faulty.

Each sensor should return a voltage between 0 and 0.1 or between 4.9 and 5.1.
(I.e. the values should be close to 0 or close to 5, with a little bit of "jitter".)

Find all of the bad values and print out:
- The name of the bad sensor.
- The number of bad voltages.
- Every bad voltage value.

Answer:
```
The bad sensor is: left
Number of bad voltages: 26
Bad voltages:
  - 3.367479206766042
  - 1.23491173669927
  - 1.7133662875668043
  - 2.446710739747313
  - 3.518772943934476
  - 1.6609643966321386
  - 2.4404255601279665
  - 3.2735178245992143
  - 1.1216843281350308
  - 3.13692067607718
  - 3.14748682574412
  - 3.645487832368286
  - 3.659131200895671
  - 1.1080799796093102
  - 1.764139874626479
  - 3.939954006390472
  - 2.2119943823370596
  - 3.963080092665278
  - 2.1612452756729503
  - 1.4813280766308592
  - 3.7518372593565923
  - 1.0687977491804292
  - 1.1434006678227187
  - 2.7312190737727398
  - 2.976974523288423
  - 1.0757317429755955
```

---

## Exercise 2

When querying a database using SQL,
it is common to combine data from 2 different tables using an "inner join".

Let's try to do something similar with Python.

The code in `ex-8-invoices.py` has some starter code.

Two files are read in: one with invoice data and one with company data.

There are 2 places where the code needs updating:
- finding the unpaid invoices
- updating the outout (with the name and phones of people to contact).


Answer:
```
Name: John Smith  Phone: +1 (555) 123-4567
Name: Michael Brown  Phone: +1 (555) 345-6789
Name: Daniel Lopez  Phone: +1 (555) 345-6789
Name: Jason Lewis  Phone: +1 (555) 789-0123
Name: Brandon Hill  Phone: +1 (555) 567-8901
Name: Christina Hernandez  Phone: +1 (555) 234-5678
Name: Nathan Anderson  Phone: +1 (555) 789-0123
Name: Amanda Lopez  Phone: +1 (555) 012-3456
```
