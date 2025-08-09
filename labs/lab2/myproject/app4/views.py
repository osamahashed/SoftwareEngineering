from django.shortcuts import render

def index(request):
	name = {"fname": "Osama"}
	
	return render(request, "index.html", name)
	
	
def home(request):

	return render(request,'home.html')
		

def list(request):
	students = {
		"name": "Osama",
		"marks": [90, 95, 98, 97],
		"eachsub": {
			"Software Engineering": 96,
			"Image processing": 94,
			"Client and Server Programming": 96
		}
	}
	return render(request, 'show.html', students)
	

def edit(request):
	students={"total":286,
		"marks":{"Software Enginnering":96,
			"Image Processing":94,
			"Clinet and Server Programming":96}
			}
	
	return render(request,'edit.html',students)
	

def delete(request):
	return render(request,'delete.html')




# Create your views here.
