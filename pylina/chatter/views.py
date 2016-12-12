import json
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.


def index(request):
#    from django import forms
#    class NameForm(forms.Form):
#        your_name = forms.CharField(label='Your name', max_length=100)
#
#    context = { "form" : NameForm() }
#    return render(request,'chatter/chatter.html',context)
    return render(request,'chatter/chatter.html')
    
class ChatterView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    def _serialize_conversation(self, session):
        if session.conversation.empty():
            return []

        conversation = []

        for statement, response in session.conversation:
            conversation.append([statement.serialize(), response.serialize()])

        return conversation

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.
        """
        input_data = json.loads(request.read().decode('utf-8'))
        self.validate(input_data)
        
        #---input data process----
        
        return JsonResponse(input_data, status=200) 

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        chat_session = self.get_chat_session(request)

        data = {
            'detail': 'You should make a POST request to this endpoint.',
            'name': self.chatterbot.name,
            'conversation': self._serialize_conversation(chat_session)
        }

        # Return a method not allowed response
        return JsonResponse(data, status=405)

    def patch(self, request, *args, **kwargs):
        """
        The patch method is not allowed for this endpoint.
        """
        data = {
            'detail': 'You should make a POST request to this endpoint.'
        }

        # Return a method not allowed response
        return JsonResponse(data, status=405)

    def delete(self, request, *args, **kwargs):
        """
        The delete method is not allowed for this endpoint.
        """
        data = {
            'detail': 'You should make a POST request to this endpoint.'
        }

        # Return a method not allowed response
        return JsonResponse(data, status=405)

    