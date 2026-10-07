from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Reporter, Issue, CriticalIssue, LowerPriorityIssue
import json

# Create this views for testing purpose.
def hello_world(request):
    return HttpResponse("Hello world")


#Create Reporter 
def create_reporter(request):

    data = json.loads(request.body)

    reporter = Reporter(
        id = data.get("id"),
        name = data.get("name"),
        email = data.get("email"),
        team = data.get("team")
    )

    reporter.validate()

    with open("reporters.json", "r") as file:
        reporters = json.load(file)
    reporters.append(reporter.to_dict())


    with open("reporters.json", "w") as file:
        json.dump(reporters, file, indent=4) 

    return JsonResponse(
        reporter.to_dict(),
        status= 201
    )



def reporters(request):
    with open("reporters.json", "r") as file:
        reporters = json.load(file)

    reporter_id = request.GET.get('id')

    if reporter_id:
        for ind_report in reporters:
            if ind_report["id"] == int(reporter_id):
                return JsonResponse(ind_report, status=200)

        return JsonResponse(
            {"error":"The record not found"},
            status = 404
        )

    #All Reporteer Record
    return JsonResponse(
        reporters, safe=False, status = 200
    )

def issues(request):
    #print("Body", request.body)
    data = json.loads(request.body)

    priority = data.get("priority")

    if priority == "Critical":
        issue = CriticalIssue(
            id = data.get("id"),
            title = data.get("title"),
            description = data.get("description"),
            status = data.get("status"),
            priority = data.get("priority"),
            reporter_id = data.get("reporter_id"),
            created_at = data.get("created_at") 
            
        )
    elif priority == "Low":
        issue = LowerPriorityIssue(
            id = data.get("id"),
            title = data.get("title"),
            description = data.get("description"),
            status = data.get("status"),
            priority = data.get("priority"),
            reporter_id = data.get("reporter_id"),
            created_at = data.get("created_at")  
                )

    else:
        issue = Issue(
            id = data.get("id"),
            title = data.get("title"),
            description = data.get("description"),
            status = data.get("status"),
            priority = data.get("priority"),
            reporter_id = data.get("reporter_id"),
            created_at = data.get("created_at") 

        )

    issue.validate()
    print(issue.describe())


    with open('issues.json', 'r') as file:
        issues = json.load(file)

    issues.append(issue.to_dict())

    with open('issues.json', 'w') as file:
        json.dump(issues, file, indent=4)

    return JsonResponse(
        issue.to_dict(),
        status = 201
    )


def all_issue(request):
    with open("issues.json", "r") as file:
        issues = json.load(file)
    issue_id = request.GET.get('id')

    if issue_id:
        for ind_issue in issues:
            if ind_issue["id"] == int(issue_id):
                return JsonResponse(ind_issue, status=200)

        return JsonResponse(
            {"error" : "Issue not found for this id"},
            status = 404
        )

    status = request.GET.get("status")
    if status:
        all_record_by_filter = []
        
        for issue in issues:
            if issue["status"] == status:
                print("got status", status)
                all_record_by_filter.append(issue)
        print(all_record_by_filter)
        
        if not all_record_by_filter:
            return JsonResponse(
                {'error' : "Status must be one of: open, in_progress, resolved, closed"},
                status = 404

            )   
        return JsonResponse(
            all_record_by_filter, safe=False, status = 200
        )

    return JsonResponse(
        issues, safe = False, status=200
    )

