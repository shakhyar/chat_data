<h1>
customizable question and answer dataset builder</h1>

<h3>Create your own chat or q&a data for deep learning models</h3>

<hr>

<p>Here, you can collect data by prompting people to input few questions and answers, or even create a custom dataset yourself by entering the data yourself. 
The data would be saved as ```pickle``` files</p>

<h3>Contents</h3>

<ul>
<li><h3>questions{counter}.p</h3>: Contains the questions saved to disk as pickle file</li>
<li><h3>answers{counter}.p</h3>: Contains the answers saved to disk as pickle file</li>
<li><h3>counter.p</h3>: Contains the metadata, i.e, number of different data files created. For example, if a counter file has something like this```[1, 2, 3]```,
that means there must be 3 different datasets, like ```questions1.p, questions2.p, questions3.p, answers1.p, answers2.p, answers3.p```. 
<br>The reason why I am using a counter files because the indexes of questions can map properly to the answers, no extra complicated mapping algorithms.<br>
Also this is helpful when you are preparing dataset for multiple domains, for example, a chatbot for programming and science related questions, so you can store all programming<br>
related q&a in ```questions1.p and answers1.p```, and science related stuffs in the next counter, or ```questions2.p and answers2.p```
</li>

