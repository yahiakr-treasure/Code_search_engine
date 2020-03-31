## Inspiration

Our team wants to help the generations after us in obtaining coding information more conveniently than what is currently possible with other search engines (_Google_,  _Bing_,  _Duck Duck Go_, etc.). There is a lot of unneeded information that is displayed when searching for coding information. For this reason, we want to make a search engine specifically designed to help students and developers find the code they need.

## What it does

Our final product takes in user input (like Google Search) and utilizes natural language processing techniques (a fine-tuned language model) to show several functions in python (with a hyperlinked GitHub repository) that relate to the user search through K means vector correlation.

## How we built it

We built our final product using a five step model:

**Step 1: Obtaining the Data**

We obtained the data from a very large dataset of GitHub repositories in Google Cloud, using  _BigQuery_, a SQL-like tool for querying big data. We limited our search to Python repositories, so we could rely on the syntax of code and comments to be specific to Python.

**Step 2: Preprocessing the data**

In order to extract all the python specific data with  _BigQuery_,  _Google Colab_  was used to convert the data into one condensed  _pandas_  table with documentations in one column and functions corresponding to the documentation in the other. In order to ultimately relate the user input (in the search engine) to specific python functions, docstrings needed to be extracted and taken apart from the GitHub README's to compare them when creating the model.

**Step 3: Running the data through the model**

After extracting all the python code with the docstrings, we started fine-tuning a language model (BERT language model) to generate embeddings for the docstrings. This way, when we get the user input, we represent it as a vector, and map it into the same vector space as the docstrings vectors, and return the “K nearest neighbors” functions associated to the k vectors.

**Step 4: Backend processing of the data**

Once we created and trained our model, we made an interface using  _Flask_. Our back-end receives the user input, processes it, and returns a list of k functions that describe the same concept.

**Step 5: Integrated back-end with the front-end**

We connected the front-end and back-end and provide the user with a readable table that consists of a list of functions and its corresponding source URL in a run time comparable to that of Google.

## My contribution
I did (realised) the steps : 3 & 4. All the notebooks that i used are included in the repository.

## Challenges we ran into

We wanted to host the app on Google’s  _AppEngine_; however, errors occurred during deployment which vastly increased the difficulty of publishing the app. We also faced severe computational limitations which limited the amount of data used to train our model.

## Accomplishments that we're proud of

We are proud of completing our own search engine! At first the team was daunted by the task of making a localized search engine in just 36 hours, but we remained steadfast, and the team’s resilience and perseverance is what pushed everyone to work in a cohesive unit while having fun. We are most proud of having a completed product after running into many different challenges, such as the difficulties of cleaning and subsetting an enormous dataset, learning to use Google Cloud Technologies, and connecting our underlying code to a sleek user interface.

## What we learned

We as a team learned much about different skills that we were not very familiar with at the start of this hackathon. For example, we learned the intricacies of BigQuery, different machine learning and data science related techniques, connecting front-end and back-end code. We were introduced to many different interfaces that we will be sure to use in the future (_Google colab_,  _Google cloud_,  _Postman_,  _appengine_, and even  _Flask_). We also learned about the importance of keeping an open mind. In the beginning this team started with just two highschoolers, and soon after, two other slots were occupied by college attendees, one whom resides in Africa. Our varied backgrounds and experience made for an interesting group dynamic, and made our successes that much more gratifying. Though making an app engine is not something any individual would try to do in just 36 hours, our team did it by staying dedicated and on task while also getting some sleep! Overall, the experience was a fantastic one and our hard work paid off with.

## What's next

DiscoverCode is implemented just for Python functions at the moment. Thus, whatever the user currently searches up (ex. how to add two numbers) will only show up for the programming language Python. We applied this restriction because we did not have ample time, or the computing power to include more data or more programming languages. For this reason, the future of DiscoverCode will be to add other programming languages to support the desires of all developers. Also, due to difficulties with Google Cloud, we were not able to deploy our website, so we had to run it locally. In the future, we will make it open to the public.

Devpost link of the project : [https://devpost.com/software/discovercode](https://devpost.com/software/discovercode)
