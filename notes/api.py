from rest_framework import serializers, viewsets
from .models import Note, PersonalNote


# TODO: Critical disable or make this only for admin
class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ('title', 'content')


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()


class PersonlNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = self.context['request'].user
        personal_note = PersonalNote.objects.create(user=user, **validated_data)
        return personal_note


class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonlNoteSerializer
    queryset = PersonalNote.objects.none()

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return queryset
        else:
            return PersonalNote.objects.filter(user=user)

