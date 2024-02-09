from flask import render_template, Blueprint, request
from difflib import SequenceMatcher  # Import SequenceMatcher

COMPARISON_TYPES = {
    'matching': {'color': 'gray'},  # Default color for matching lines
    'added': {'color': 'green'},   # Color for lines added to text2
    'deleted': {'color': 'red'}    # Color for lines deleted from text2
}

comparar_bp = Blueprint('comparar', __name__)

@comparar_bp.route('/compare', methods=['POST'])
def compare_texts():
    text1 = request.form['text1']
    text1_lines = text1.splitlines()  # Divide text1 en líneas

    text2 = request.form['text2']
    text2_lines = text2.splitlines()  # Divide text2 en líneas

    # Similarity threshold
    SIMILARITY_THRESHOLD = 0.85

    combined_lines = []

    # For each line in text1, find the most similar line in text2
    for line1 in text1_lines:
        best_match = None
        best_match_ratio = 0
        for line2 in text2_lines:
            matcher = SequenceMatcher(None, line1, line2)
            ratio = matcher.ratio()
            if ratio >= SIMILARITY_THRESHOLD and ratio > best_match_ratio:
                best_match = line2
                best_match_ratio = ratio

        # Determine the type of line (matching, added, deleted)
        if best_match:
            combined_lines.append({'text1': line1, 'text2': best_match, 'type': 'matching'})
            text2_lines.remove(best_match)  # Remove the matched line from text2
        else:
            combined_lines.append({'text1': line1, 'text2': '', 'type': 'deleted'})

    # Add remaining lines in text2 (added lines)
    for line2 in text2_lines:
        combined_lines.append({'text1': '', 'text2': line2, 'type': 'added'})

    return render_template('comparar.html', combined_lines=combined_lines, comparison_types=COMPARISON_TYPES)

# import difflib
# from flask import render_template, Blueprint, request, jsonify
# import diff_match_patch
# from difflib import SequenceMatcher

# # Define un umbral de similitud para considerar líneas similares
# SIMILARITY_THRESHOLD = 0.8

# comparar_bp = Blueprint('comparar', __name__)

# @comparar_bp.route('/')
# def read_comparar():
#     return render_template('comparar.html')

# @comparar_bp.route('/compare', methods=['POST'])
# def compare_texts():
#     text1 = request.form['text1']
#     text2 = request.form['text2']

#     dmp = diff_match_patch.diff_match_patch()
#     dmp.Diff_Timeout = 0

#     diffs = dmp.diff_main(text1, text2)
#     dmp.diff_cleanupSemantic(diffs)

#     matching_lines = []
#     for line1 in text1.splitlines():
#         for line2 in text2.splitlines():
#             matcher = SequenceMatcher(None, line1, line2)

#             if matcher.ratio() >= SIMILARITY_THRESHOLD:
#                 matching_lines.append(line1)

#     print(matching_lines)   
#     return jsonify({'matching_lines': matching_lines})

    # for diff in diffs:
    #     operation, text = diff

    #     if operation == diff_match_patch.diff_match_patch.DIFF_EQUAL:  # Líneas iguales
    #         matching_lines.append(text)
    #     elif operation == diff_match_patch.diff_match_patch.DIFF_DELETE:  # Línea eliminada
    #         # No se incluye
    #         pass
    #     else:  # Línea insertada o modificada
    #         # Separa la línea en tokens usando split
    #         tokens = text.split()

    #         # Busca coincidencias parciales usando el método split
    #         matching_sublines = []
    #         for token in tokens:
    #             if token in text1 or token in text2:    
    #                 matching_sublines.append(token)

    #         # Si hay coincidencias parciales, agrega la línea original
    #         if matching_sublines:
    #             matching_lines.append(' '.join(matching_sublines))

    # print(matching_lines)
    # return jsonify({'matching_lines': matching_lines})

