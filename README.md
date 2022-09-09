# Recommendation-System-on-MovieLens-Dataset

Project assignment of Recommendation System course in Taiwan, NDHU CSIE. This system using user-based collaborative filtering technique to make recommendation. 

----

## About-MovieLens-Dataset

MovieLens data sets were collected by the GroupLens Research Project
at the University of Minnesota.

This data set consists of:

* 100,000 ratings (1-5) from 943 users on 1682 movies.
* Each user has rated at least 20 movies.
* Simple demographic info for the users (age, gender, occupation, zip)

The data was collected through the MovieLens web site
(movielens.umn.edu) during the seven-month period from September 19th,
1997 through April 22nd, 1998. This data has been cleaned up - users
who had less than 20 ratings or did not have complete demographic
information were removed from this data set. Further descriptions regarding this dataset can be found [here](http://files.grouplens.org/datasets/movielens/ml-100k-README.txt).

## User-Based Collaborative Recommendation System

Collaborative filtering is mainly divided into two categories, memory-based and model-based. User-based collaborative filtering classified as memory-based, which is computation of historical record. User-based collaborative filtering makes recommendations based on user-product interactions in the past. The assumption behind the algorithm is that similar users like similar products. There are different ways to measure similarities. Pearson correlation and cosine similarity are two widely used methods. In this project, using cosine similarity to calculate similarity of two users, then predict how much item rating that user will give.
## CITATION

==============================================

To acknowledge use of the dataset in publications, please cite the
following paper:

F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets:
History and Context. ACM Transactions on Interactive Intelligent
Systems (TiiS) 5, 4, Article 19 (December 2015), 19 pages.
DOI=<http://dx.doi.org/10.1145/2827872>
