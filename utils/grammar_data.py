"""Grammar exercises data access layer"""

from data.grammar_exercises import GRAMMAR_EXERCISES

class GrammarData:
    """Class to access and manage grammar exercises"""
    
    def __init__(self):
        self.data = GRAMMAR_EXERCISES
    
    def get_topics(self):
        """Get all grammar topics with metadata"""
        topics = []
        for topic_id, topic_data in self.data.items():
            topics.append({
                'id': topic_id,
                'title': topic_id,
                'description': topic_data['description'],
                'difficulty': topic_data['difficulty'],
                'exercise_count': len(topic_data['exercises'])
            })
        return topics
    
    def get_topic_by_id(self, topic_id):
        """Get a specific grammar topic by ID"""
        topic_data = self.data.get(topic_id)
        if topic_data:
            return {
                'id': topic_id,
                'title': topic_id,
                'description': topic_data['description'],
                'difficulty': topic_data['difficulty'],
                'explanation': topic_data['explanation'],
                'exercises': topic_data['exercises'],
                'examples': topic_data.get('examples', [])
            }
        return None
    
    def get_topics_by_difficulty(self, difficulty):
        """Get topics filtered by difficulty level"""
        topics = []
        for topic_id, topic_data in self.data.items():
            if topic_data['difficulty'] == difficulty:
                topics.append({
                    'id': topic_id,
                    'title': topic_id,
                    'description': topic_data['description'],
                    'difficulty': topic_data['difficulty']
                })
        return topics
    
    def get_difficulties(self):
        """Get list of unique difficulty levels"""
        difficulties = set()
        for topic_data in self.data.values():
            difficulties.add(topic_data['difficulty'])
        return sorted(list(difficulties))
