from flask import render_template, Blueprint, request
import diff_match_patch

comparar_bp = Blueprint('comparar', __name__)

@comparar_bp.route('/')
def read_comparar():
    return render_template('comparar.html')

@comparar_bp.route('/compare', methods=['POST'])
def compare_texts():
    text1 = request.form['text1']
    text2 = request.form['text2']

    # Create a diff_match_patch object
    dmp = diff_match_patch.diff_match_patch()

    # All 'diff' jobs start with invoking diff_main()
    diffs = dmp.diff_main(text1, text2)

    # And if you want the results as some ready to display HTML snippet
    htmlSnippet_text1 = text1
    htmlSnippet_diffs = dmp.diff_prettyHtml(diffs)

    # Render the template with the data
    return htmlSnippet_diffs


# from flask import render_template, Blueprint, request
# import diff_match_patch

# comparar_bp = Blueprint('comparar', __name__)

# @comparar_bp.route('/')
# def read_comparar():
#     return render_template('comparar.html')

# @comparar_bp.route('/compare', methods=['POST'])
# def compare_texts():
#     text1 = request.form['text1']
#     text2 = request.form['text2']

#     # Create a diff_match_patch object
#     dmp = diff_match_patch.diff_match_patch()

#     # Depending on the kind of text you work with, in term of overall length
#     # and complexity, you may want to extend (or here suppress) the
#     # time_out feature
#     dmp.Diff_Timeout = 0   # or some other value, default is 1.0 seconds

#     # All 'diff' jobs start with invoking diff_main()
#     diffs = dmp.diff_main(text1, text2)

#     # diff_cleanupSemantic() is used to make the diffs array more "human" readable
#     dmp.diff_cleanupSemantic(diffs)

#     # And if you want the results as some ready to display HTML snippet
#     htmlSnippet = dmp.diff_prettyHtml(diffs)

#     return htmlSnippet



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