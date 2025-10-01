"""Conversation scenarios data access layer"""

from data.conversation_scenarios import CONVERSATION_SCENARIOS

class ConversationData:
    """Class to access and manage conversation scenarios"""
    
    def __init__(self):
        self.data = CONVERSATION_SCENARIOS
    
    def get_scenarios(self):
        """Get all conversation scenarios with metadata"""
        scenarios = []
        for scenario_id, scenario_data in self.data.items():
            scenarios.append({
                'id': scenario_id,
                'title': scenario_id,
                'description': scenario_data['description'],
                'difficulty': scenario_data['difficulty'],
                'dialogue_length': len(scenario_data['dialogue'])
            })
        return scenarios
    
    def get_scenario_by_id(self, scenario_id):
        """Get a specific scenario by ID"""
        scenario_data = self.data.get(scenario_id)
        if scenario_data:
            return {
                'id': scenario_id,
                'title': scenario_id,
                'context': scenario_data['description'],
                'difficulty': scenario_data['difficulty'],
                'conversation': scenario_data['dialogue'],
                'key_phrases': scenario_data.get('key_phrases', []),
                'practice_points': scenario_data.get('practice_points', [])
            }
        return None
    
    def get_scenarios_by_difficulty(self, difficulty):
        """Get scenarios filtered by difficulty level"""
        scenarios = []
        for scenario_id, scenario_data in self.data.items():
            if scenario_data['difficulty'] == difficulty:
                scenarios.append({
                    'id': scenario_id,
                    'title': scenario_id,
                    'description': scenario_data['description'],
                    'difficulty': scenario_data['difficulty']
                })
        return scenarios
    
    def get_difficulties(self):
        """Get list of unique difficulty levels"""
        difficulties = set()
        for scenario_data in self.data.values():
            difficulties.add(scenario_data['difficulty'])
        return sorted(list(difficulties))
