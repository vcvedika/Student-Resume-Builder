from django import forms
from .models import resume, Education, PersonalInfo, Skills, Projects, Achievements


class PersonalInfoForm(forms.ModelForm):

    class Meta:

        model = PersonalInfo
        fields = ('first_name', 'last_name',
                  'address', 'email', 'github', 'linkedin',)

        widgets = {
            'first_name': forms.TextInput(attrs={'title': 'First Name'}),
            'last_name': forms.TextInput(attrs={'title': 'Last Name'}),
            'address': forms.Textarea(attrs={'title': 'Address'}),
            'email': forms.EmailInput(attrs={'title': 'Email'}),
            'github': forms.URLInput(attrs={'title': 'Github'}),
            'linkedin': forms.URLInput(attrs={'title': 'LinkedIn'}),
        }


class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ('varsity_name', 'degree', 'stream', 'passing_year', 'result', 'school10_name', 'board10', 'passing_year10', 'result10', 'school12_name', 'board12', 'passing_year12', 'result12')
        widgets = {
            'degree': forms.TextInput(attrs={'title': 'Degree'}),
            'stream': forms.TextInput(attrs={'title': 'Stream'}),
            'passing_year': forms.TextInput(attrs={'title': 'Passing Date'}),
            'result': forms.TextInput(attrs={'title': 'Result'}),
            'school10_name': forms.TextInput(attrs={'title': 'School 10'}),
            'board10': forms.TextInput(attrs={'title': 'Board 10'}),
            'passing_year10': forms.TextInput(attrs={'title': 'Passing Date 10'}),
            'result10': forms.TextInput(attrs={'title': 'Result 10'}),
            'school12_name': forms.TextInput(attrs={'title': 'School 12'}),
            'board12': forms.TextInput(attrs={'title': 'Board 12'}),
            'passing_year12': forms.TextInput(attrs={'title': 'Passing Date 12'}),
            'result12': forms.TextInput(attrs={'title': 'Result 12'}),
        }


class SkillsForm(forms.ModelForm):

    class Meta:
        model = Skills
        fields = ('skill_detail',)
        widgets = {

            'skill_detail': forms.Textarea(attrs={'title': 'Skill_detail'})
        }


class ProjectsForm(forms.ModelForm):

    class Meta:
        model = Projects
        fields = ('project_detail',)
        widgets = {

            'project_detail': forms.Textarea(attrs={'title': 'Project_detail'})
        }


class AchievementsForm(forms.ModelForm):

    class Meta:
        model = Achievements
        fields = ('achievement_detail',)
        widgets = {

            'achievement_detail': forms.Textarea(attrs={'title': 'Achievement_detail'})
        }


class resumeForm(forms.ModelForm):

    class Meta:
        model = resume
        fields = ('first_name', 'last_name',
                  'address', 'email', 'github', 'linkedin', 'website',)
        