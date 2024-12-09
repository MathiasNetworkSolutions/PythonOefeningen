This is to get my own repos from github without tokens:  
(link: https://api.github.com/  )



get all repos from myself:  
(link: curl https://api.github.com/users/<gebruikersnaam>/repos
	"https://api.github.com/repos/{owner}/{repo}" )  


https://api.github.com/users/MathiasNetworkSolutions/repos 


get all commits from specific repo:  
(syntax: https://api.github.com/repos/MathiasNetworkSolutions/<repo-naam>/commits  
"https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}"  )  
https://api.github.com/repos/MathiasNetworkSolutions/PythonOefeningen/commits

url om alle openbare repos op te halen in github die met python zijn geschreven:  
"https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}"  
https://api.github.com/search/repositories?q=language:python
