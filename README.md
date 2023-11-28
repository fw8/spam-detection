# Personal SPAM detection

[![Open in DevPod!](https://devpod.sh/assets/open-in-devpod.svg)](https://devpod.sh/open#https://github.com/fw8/spam-detection)

As I was experimenting with machine learning, I began to consider whether it could be used to tidy up my personal email inbox. My idea was to categorize unwanted spam emails into a folder labeled `LearnSpam` and also classify good emails (non-spam) into a folder called `LearnHam`.

While most of the spam is already detected by my rspamd, there are still some emails that I don't want to receive. To make it easier to identify and sort out these unwanted emails, I decided to train a model with my personal data from the `LearnSpam` and `LearnHam` folders. Once the model is trained, I apply it to my inbox and flag any emails that the model identifies as spam.

Using my mail client, I can select the flagged emails and review them to determine if there are any false positives that I can add to the 'LearnHam' folder for the next round of training.

Overall, the results of my experimentation have been promising. While I acknowledge that this is a very simple approach, I see it as my playground to explore and experiment with machine learning.
