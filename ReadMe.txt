
Question 2:

i) BackPropogation:

    BackPropogation is a technique used to improve ou model accuracy. In deep learning models after trained our data we check for
loss. Loss is nothing but the difference between the actuall vlaue and the predicted value. Also we call it as errors. And to find the error 
or loss we do calculate loss function also known as cost function. Our main objective is to optimize the cost function. If the loss is very 
less our model is that very good. To optimze our loss funciton we do back propogation. It is simply calculates  the gradient of the loss function
When training a neural network by gradient descent, a loss function is calculated, which represents how far the network's predictions are from the 
true labels.
    BackPropogation work from the last layer to the first layer.It efficiently computes one layer at a time, unlike a native direct computation. 
It computes the gradient, but it does not define how the gradient is used. It generalizes the computation in the delta rule.






ii)
    Handling missing values is one of the main core problem in machine learning models. The imputation of NaN values should be handle carfully.
40 percentage of missing values is noticable problem. We can't just drop the records having missing values. 

******Step 1:

    First we need to do exploratory data analysis. By creating visuals we should do multivariate and univariate analysis. To check whether the 4 columns are
having good relation with the dependent variabl (Target variable). This step also involves, correlation analysis. If the features are categorical we need to do
chi square test.

---------Need for this step: -------------
        If the 4 columns are not descriminat features we don't want to consider them. And we are free from imputation.
        If the 4 columns are important and some of the 4 columns are important we need to move further.

******Step 2:

    If it is Numerical feature (float/int) we can fill the missing value by mean, median, mode. 
    If it is Categorical feature (object) we can fill the missing values by most frequent(mode)/ we can create a new category named "unknown" or "others"
for the missing values.
    If the particular feature contains binary values.. we can use logistic regression to predict the missing values
    If the particular feature contains continous values we can use linear regression or some other regression algorithms to find the missing values.
