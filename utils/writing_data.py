"""Writing exercises data access layer"""

from data.writing_prompts import WRITING_PROMPTS

class WritingData:
    """Class to access and manage writing exercises"""
    
    def __init__(self):
        self.data = WRITING_PROMPTS
    
    def get_exercises(self):
        """Get all writing exercises with metadata"""
        exercises = []
        for exercise_id, exercise_data in self.data.items():
            exercises.append({
                'id': exercise_id,
                'title': exercise_id,
                'type': exercise_data['type'],
                'difficulty': exercise_data['difficulty'],
                'scenario': exercise_data['scenario'],
                'focus_skills': self._extract_focus_skills(exercise_data)
            })
        return exercises
    
    def get_exercise_by_id(self, exercise_id):
        """Get a specific writing exercise by ID"""
        exercise_data = self.data.get(exercise_id)
        if exercise_data:
            return {
                'id': exercise_id,
                'title': exercise_id,
                'type': exercise_data['type'],
                'difficulty': exercise_data['difficulty'],
                'scenario': exercise_data['scenario'],
                'task': exercise_data.get('scenario', ''),
                'guidelines': exercise_data.get('guidelines', []),
                'requirements': exercise_data.get('guidelines', []),
                'model_answer': exercise_data.get('sample_answer', ''),
                'key_features': self._extract_key_features(exercise_data),
                'useful_phrases': self._extract_useful_phrases(exercise_data),
                'improvement_tips': exercise_data.get('guidelines', [])
            }
        return None
    
    def get_exercises_by_type(self, exercise_type):
        """Get exercises filtered by type"""
        exercises = []
        for exercise_id, exercise_data in self.data.items():
            if exercise_data['type'] == exercise_type:
                exercises.append({
                    'id': exercise_id,
                    'title': exercise_id,
                    'type': exercise_data['type'],
                    'difficulty': exercise_data['difficulty']
                })
        return exercises
    
    def get_exercises_by_difficulty(self, difficulty):
        """Get exercises filtered by difficulty level"""
        exercises = []
        for exercise_id, exercise_data in self.data.items():
            if exercise_data['difficulty'] == difficulty:
                exercises.append({
                    'id': exercise_id,
                    'title': exercise_id,
                    'type': exercise_data['type'],
                    'difficulty': exercise_data['difficulty']
                })
        return exercises
    
    def get_types(self):
        """Get list of unique exercise types"""
        types = set()
        for exercise_data in self.data.values():
            types.add(exercise_data['type'])
        return sorted(list(types))
    
    def get_difficulties(self):
        """Get list of unique difficulty levels"""
        difficulties = set()
        for exercise_data in self.data.values():
            difficulties.add(exercise_data['difficulty'])
        return sorted(list(difficulties))
    
    def _extract_focus_skills(self, exercise_data):
        """Extract focus skills from exercise data"""
        # Extract from key phrases or guidelines
        if 'key_phrases' in exercise_data:
            return exercise_data['key_phrases'][:3]  # First 3 key phrases as skills
        elif 'guidelines' in exercise_data:
            return exercise_data['guidelines'][:3]
        return ['Professional Writing', 'Business Communication']
    
    def _extract_key_features(self, exercise_data):
        """Extract key features from model answer"""
        if 'key_phrases' in exercise_data:
            return [f"Uses phrase: '{phrase}'" for phrase in exercise_data['key_phrases'][:5]]
        return [
            'Professional tone and structure',
            'Clear and concise language',
            'Appropriate greeting and closing',
            'Well-organized information',
            'Courteous and helpful approach'
        ]
    
    def _extract_useful_phrases(self, exercise_data):
        """Extract useful phrases organized by category"""
        if 'key_phrases' in exercise_data:
            return {
                'Opening': [exercise_data['key_phrases'][0]] if len(exercise_data['key_phrases']) > 0 else [],
                'Main Content': exercise_data['key_phrases'][1:-1] if len(exercise_data['key_phrases']) > 2 else [],
                'Closing': [exercise_data['key_phrases'][-1]] if len(exercise_data['key_phrases']) > 0 else []
            }
        return {
            'Opening': [
                'Thank you for your email/inquiry',
                'I hope this email finds you well',
                'I am writing to...'
            ],
            'Main Content': [
                'I would like to inform you that...',
                'Please note that...',
                'As requested, here is...'
            ],
            'Closing': [
                'If you have any questions, please don\'t hesitate to contact us',
                'We look forward to hearing from you',
                'Thank you for your time and consideration'
            ]
        }
