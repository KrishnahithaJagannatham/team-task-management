def get_priority_color(priority):
    colors = {
        'High': 'text-red-600 bg-red-100',
        'Medium': 'text-yellow-600 bg-yellow-100',
        'Low': 'text-green-600 bg-green-100'
    }
    return colors.get(priority, 'text-gray-600 bg-gray-100')