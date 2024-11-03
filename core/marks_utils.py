import ast


def compare_grades(new_grades: list, old_grades: list) -> list:
    """
    Compare les notes
    :param new_grades: Nouvelle note qui provient de l'API
    :param old_grades: Ancienne note qui provient de la base de données
    :return:
    """
    obj_to_return = []
    for new_grade_dict in new_grades:
        for old_grade_dict in old_grades:
            if new_grade_dict.get('course') == old_grade_dict.get('course'):
                new_grade_list = new_grade_dict.get('grades')
                old_grade_list = old_grade_dict.get('grades')
                for new_grade in new_grade_list:
                    if new_grade and len(ast.literal_eval(old_grade_list)) == 0:
                        obj_to_return.append({
                            'course': new_grade_dict.get('course'),
                            'grades': new_grade_list,
                        })
                    for old_grade in ast.literal_eval(old_grade_list):
                        if new_grade != old_grade:
                            obj_to_return.append({
                                'course': new_grade_dict.get('course'),
                                'grades': new_grade_list,
                            })
    print("obj_to_return", obj_to_return)
    return obj_to_return


def compare_exams(obj1: list, obj2: list) -> dict:
    """
    Compare les notes d'examens
    :param new_grades: Nouvelle note qui provient de l'API
    :param old_grades: Ancienne note qui provient de la base de données
    :return:
    """
    for obj1Elt in obj1:
        for obj2Elt in obj2:
            if obj1Elt.get('exam') is None:
                return None
            if obj1Elt.get('exam') == '':
                return None
            if str(obj1Elt.get('exam')) != str(obj2Elt.get('exam')):
                obj_to_return = {
                    'course': obj1Elt.get('course'),
                    'exam': obj1Elt.get('exam'),
                }
                print("obj_to_return", obj_to_return)
                return obj_to_return
    return None
