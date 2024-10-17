import ast


def str_to_dict(arr):
    """
    Converti un tableau de string en tableau de dictionnaire
    :param arr: Array
    :return: Array
    """
    new_arr = []
    for key in arr:
        k = key.get('grades')
        if isinstance(k, str):
            try:
                for elt in ast.literal_eval(k):
                    new_arr.append(elt)
            except (ValueError, SyntaxError):
                print(f"Erreur lors de la conversion de old_grade: {k}")
    return new_arr


def equality_check(arr1, arr2, size1, size2):
    """
    Compare deux tableaux
    :param arr1: Array 1
    :param arr2: Array 2
    :param size1: Size of array 1
    :param size2: Size of array 2
    :return: Boolean
    """
    if size1 != size2:
        return False
    arr1.sort()
    arr2.sort()
    for i in range(0, size2):
        if arr1[i] != arr2[i]:
            return False
    return True


def compare_grades(new_grades, old_grades):
    """
    Compare les notes
    :param new_grades: dict
    :param old_grades: dict
    :return:
    """
    old_grades_dict = str_to_dict(old_grades)

    for _ in old_grades_dict:
        for new_grade_dict in new_grades:
            new_grade_list = new_grade_dict.get('grades')
            course = new_grade_dict.get('course')
            if not equality_check(new_grade_list, old_grades_dict, len(new_grade_list), len(old_grades_dict)):
                obj_to_return = {
                    'course': course,
                    'grades': new_grade_list,
                }
                return obj_to_return
            return None


def compare_exams(obj1, obj2):
    """
    Compare les notes d'examens
    :param new_grades: dict
    :param old_grades: dict
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
                return obj_to_return
    return None
