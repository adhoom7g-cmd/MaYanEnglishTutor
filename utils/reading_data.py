"""Reading comprehension data access layer"""

from data.reading_content import READING_CONTENT

class ReadingData:
    """Class to access and manage reading comprehension content"""
    
    def __init__(self):
        self.data = READING_CONTENT
    
    def get_passages(self):
        """Get all reading passages with metadata"""
        passages = []
        for passage_id, passage_data in self.data.items():
            word_count = len(passage_data['text'].split())
            passages.append({
                'id': passage_id,
                'title': passage_id,
                'type': passage_data['type'],
                'difficulty': passage_data['difficulty'],
                'word_count': word_count,
                'question_count': len(passage_data['questions']),
                'topic': passage_data.get('type', 'General'),
                'description': f"{passage_data['type']} - {passage_data['difficulty']} level"
            })
        return passages
    
    def get_passage_by_id(self, passage_id):
        """Get a specific reading passage by ID"""
        passage_data = self.data.get(passage_id)
        if passage_data:
            word_count = len(passage_data['text'].split())
            return {
                'id': passage_id,
                'title': passage_id,
                'type': passage_data['type'],
                'difficulty': passage_data['difficulty'],
                'text': passage_data['text'],
                'questions': passage_data['questions'],
                'word_count': word_count,
                'topic': passage_data.get('type', 'General'),
                'vocabulary_help': passage_data.get('vocabulary_focus', {}),
                'discussion_questions': passage_data.get('discussion_questions', [])
            }
        return None
    
    def get_passages_by_type(self, content_type):
        """Get passages filtered by content type"""
        passages = []
        for passage_id, passage_data in self.data.items():
            if passage_data['type'] == content_type:
                passages.append({
                    'id': passage_id,
                    'title': passage_id,
                    'type': passage_data['type'],
                    'difficulty': passage_data['difficulty']
                })
        return passages
    
    def get_passages_by_difficulty(self, difficulty):
        """Get passages filtered by difficulty level"""
        passages = []
        for passage_id, passage_data in self.data.items():
            if passage_data['difficulty'] == difficulty:
                passages.append({
                    'id': passage_id,
                    'title': passage_id,
                    'type': passage_data['type'],
                    'difficulty': passage_data['difficulty']
                })
        return passages
    
    def get_types(self):
        """Get list of unique content types"""
        types = set()
        for passage_data in self.data.values():
            types.add(passage_data['type'])
        return sorted(list(types))
    
    def get_difficulties(self):
        """Get list of unique difficulty levels"""
        difficulties = set()
        for passage_data in self.data.values():
            difficulties.add(passage_data['difficulty'])
        return sorted(list(difficulties))
