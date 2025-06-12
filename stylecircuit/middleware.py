from datetime import datetime


class FindLoadingTime:
    def __init__(self,get_reponse):
        self.get_reponse = get_reponse

    def __call__(self, request):
        starting_time = datetime.now().timestamp()

        response = self.get_reponse(request)

        if request.POST:
        	print(request.POST.get('password'))

        ending_time = datetime.now().timestamp()

        loading_time = ending_time - starting_time

        print(f"the total time taken is {loading_time:.2f}")


        return response
