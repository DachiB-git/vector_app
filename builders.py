from tkinter import *
from tkinter import ttk


class ElementBuilder:
    parent = None
    element = None
    position = None
    span = None
    scale = ""

    def __init__(self, parent):
        self.parent = parent

    def build(self):
        return self

    def get_element(self):
        return self.element

    def set_width(self, width):
        self.element.configure(width=width)
        return self

    def set_position(self, position):
        self.position = position
        return self

    def set_span(self, span):
        self.span = span
        return self

    def set_scale(self, scale):
        self.scale = scale
        return self

    def place_element(self):
        (row, col) = (0, 0) if self.position is None else self.position
        (row_span, col_span) = (1, 1) if self.span is None else self.span
        self.element.grid(row=row, column=col, rowspan=row_span, columnspan=col_span, sticky=self.scale)
        return self


class FrameBuilder(ElementBuilder):
    geometry = (0, 0)

    def build(self):
        self.element = Frame(self.parent)
        return self

    def set_height(self, height):
        self.element.configure(height=height)
        return self

    def set_bg(self, color):
        self.element.configure(background=color)
        return self

    def set_geometry(self, geometry):
        self.geometry = geometry
        return self

    # sets the given weight to the rowXcolumn grid array
    def set_scaling_uniform(self, weight):
        (rows, cols) = self.geometry
        for row in range(rows):
            self.element.rowconfigure(row, weight=weight)
        for col in range(cols):
            self.element.columnconfigure(col, weight=weight)
        return self

    # ([row_indices], [row_weights]), ([column_indices], [column_weights])
    # TODO : fix this shit lmao
    def set_scaling_non_uniform(self, row_indices, row_weights, col_indices, col_weights):
        for i in range(len(row_indices)):
            self.element.rowconfigure(row_indices[i], weight=row_weights[i])
        for j in range(len(col_indices)):
            self.element.columnconfigure(col_indices[j], weight=col_weights[j])
        return self


class ButtonBuilder(ElementBuilder):

    def build(self):
        self.element = ttk.Button(self.parent)
        return self

    def set_text(self, text):
        self.element.configure(text=text)
        return self

    def set_command(self, f):
        self.element.configure(command=f)
        return self


class LabelBuilder(ElementBuilder):
    def build(self):
        self.element = ttk.Label(self.parent)

    def set_text(self, text):
        self.element.configure(text=text)
        return self


class EntryBuilder(ElementBuilder):
    def build(self):
        self.element = ttk.Entry(self.parent)
        return self

    def set_font(self, font):
        self.element.configure(font=font)
        return self

    def set_state(self, state):
        self.element.state([state])
        return self
# class LabeledEntryBuilder(EntryBuilder):

# class ScrollPanelBuilder(ElementBuilder):
#     text = None
#     scroll_bar = None
#
#     def __init__(self, input, parent, width, height):
#         super().__init__(parent)
#         self.scroll_bar = Scrollbar(self.parent)
#         self.text = TextForScrollPanel(input, parent, width, height, self.scroll_bar).get_as_text()
#
#         self.scroll_bar.config(command=self.text.yview)
#
#
# class TextForScrollPanel:
#     text = None
#
#     def __init__(self, input, root, width, height, scroll_bar):
#         temp = ""
#         for k, v in input.items():
#             temp += v + "\n"
#         self.text = Text(root, width=width, height=height, yscrollcommand=scroll_bar.set)
#
#     def get_as_text(self):
#         return self.text
