# from docxtpl import DocxTemplate, InlineImage
# from docx.shared import Mm
#
# # 读取指定位置的模板文件
# doc = DocxTemplate("./test.docx")
# # 渲染的内容
# context = {
#     # 标题
#     'title': "人员信息",
#     # 表格
#     'table': [
#         {"name": "小李", "age": 11},
#         {"name": "小张", "age": 21},
#         {"name": "小张", "age": 20},
#         {"name": "小张1", "age": 10},
#         {"name": "小张2", "age": 30},
#         {"name": "小张3", "age": 40},
#     ],
#     # 页眉
#     'header': 'xxx公司人员信息管理',
#     # 页脚
#     'footer': '1',
#     # 图片
#     'image': InlineImage(doc, 'test.jpg', height=Mm(10)),
# }
# # 渲染模板
# doc.render(context)
# # 保存渲染的文件
# doc.save("generated_doc.docx")
