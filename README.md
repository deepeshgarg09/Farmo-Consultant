# Farmo-Consultant

![Home page_1](https://github.com/ruhiawasthi/Farmo-Consultant/blob/main/farmo/Farmo_1.png)

Farmers have always been the back-bone of our country & the Government is striving to strengthen this back-bone of the country through innovative and solid measures.

As we know that Agriculture is a major contributor to the economy. The mainstream Indian population depends either explicitly or implicitly on agriculture for their livelihood. It is, thus, irrefutable that agriculture plays a vital role in the country. A vast majority of the Indian farmers believe in depending on their intuition to decide which crop to sow in a particular season.

We know that a farmer’s decision about which crop to grow is generally clouded by his intuition and other irrelevant factors like making instant profits, lack of awareness about market demand, overestimating a soil’s potential to support a particular crop, and so on. A very misguided decision on the part of the farmer could place a significant strain on his family’s financial condition. 

Perhaps this could be one of the many reasons contributing to the countless suicide cases of farmers that we hear from media on a daily basis. 

![Home page_2](https://github.com/ruhiawasthi/Farmo-Consultant/blob/main/farmo/Farmo_2.png)

In a country like India, where agriculture and related sectors contribute to approximately 20.4 percent of its Gross Value Added (GVA) , such an erroneous judgment would have negative implications on not just the farmer’s family, but the entire economy of a region. 
For this reason, we have identified a farmer’s dilemma about which crop to grow during a particular season, as a very grave one.

The need of the hour is to design a system that could provide predictive insights to the Indian farmers,thereby helping them make an informed decision about which crop to grow.

With this in mind, we propose Farmo-Consultant- an intelligent system that would consider environmental parameters (temperature, rainfall) and soil characteristics.


![Home page_3](https://github.com/ruhiawasthi/Farmo-Consultant/blob/main/farmo/Farmo_4.png)

# What it does

We have successfully proposed and implemented an intelligent crop recommendation system, which can be easily used by farmers all over India. This system would assist the farmers in making an informed decision about which crop to grow depending on a variety of environmental and geographical factors.
The proposed system takes into consideration the data related to soil, weather and past year production and suggests which are the best profitable crops which can be cultivated in the apropos environmental condition. As the system lists out all possible crops, it helps the farmer in decision making of which crop to cultivate. Also, this system takes into consideration the past production of data which will help the farmer get insight into the demand and the cost of various crops in market. As maximum types of crops will be covered under this system, farmer may get to know about the crop which may never have been cultivated.


![Home page_4](https://github.com/ruhiawasthi/Farmo-Consultant/blob/main/farmo/Farmo_5.png)

# How it is built

#### Data Pre-Processing : 

This is a two-step process. The first step is to remove the missing values which were represented by a dot (‘.’) in the original dataset. The presence of these missing values deteriorates the value of the data and subsequently hampers the performance of machine learning models. Hence, in order to deal with these missing values, we replace them with large negative values, which the trained model can easily treat as outliers. 
The second step before the data is ready to be applied to machine learning algorithms is to generate class labels. Since we intend to use supervised learning, class labels are necessary. The original dataset did not come with labels, and hence we had to create them during the data preprocessing phase.

#### Applied Machine Learning Algorithms : 

Since in the proposed model, more than one class can be assigned to a single     instance, Multi-label classification (MLC) would be the ideal choice. Decision Tree, K Nearest Neighbor (K-NN), Random Forest and Naive Bayes are four machine learning algorithms that have in-built support for MLC. We also tried different Machine Learning Algorithms but we got some less accuracy only in the decision tree we got 80.65%, using Random forest we got (74.62),  KNN(71.12), Naive Bayes(65.02) of accuracy


#### Trained Model and Crop Recommendations : 

After applying the data to different machine learning algorithms, we obtain trained models of the crop recommendation system. The weights of this model can then be saved, and the farmers can easily avail crop recommendations by giving their farm’s Soil type, Rainfall, temperature, Ground water availability and season as the input to the system. 

#### Deployment 

Deployment of an ML-model simply means the integration of the model into an existing production environment which can take in an input and return an output that can be used in making practical business decisions. So we used flask and flask is a web framework.  flask provides tools, libraries, and technologies that allow us to build a web application.

# What's next for Farmo-Consultant

## Future Aspects :

### Alternate Crops Recommendation System:

Artificial Intelligence (AI) based Alternate Crop or Crop Rotation proposition is desired for providing suggestions for alternate crops which may increase profitability of the farmers by increasing the crop yield and maintaining the fertility of soil . 

### Farmer Chat-Bot:

Additionally, CHATBOTS can be introduced along with this system which is a conversational virtual assistant and provides farmers the better opportunity to obtain the desired information and to scale up with upcoming market trends and technologies in a user friendly manner.

# License
This project is under MIT License copyright [@Deepesh Garg](https://www.github.com/deepeshgarg09) and [@Ruhi Awasthi](https://www.github.com/ruhiawasthi)
