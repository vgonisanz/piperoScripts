#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.7.2 on Tue May 24 20:18:12 2016
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
import os

wildcard = "Python source (*.py)|*.py|" \
            "All files (*.*)|*.*"
# end wxGlade


class Video2GifFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Video2GifFrame.__init__
        wx.Frame.__init__(self, *args, **kwds)
        self.title_label = wx.StaticText(self, wx.ID_ANY, _("Select options to process"))
        self.input_filepath_label = wx.StaticText(self, wx.ID_ANY, _("Input file:"), style=wx.ALIGN_CENTER)
        self.input_file_textctrl = wx.TextCtrl(self, wx.ID_ANY, "")
        self.file_input_button = wx.Button(self, wx.ID_ANY, _("..."))
        self.output_filepath_label = wx.StaticText(self, wx.ID_ANY, _("Output file:"), style=wx.ALIGN_CENTER)
        self.output_file_textctrl = wx.TextCtrl(self, wx.ID_ANY, "")
        self.file_output_button = wx.Button(self, wx.ID_ANY, _("..."))
        self.fps_label = wx.StaticText(self, wx.ID_ANY, _("Fps:"), style=wx.ALIGN_CENTER)
        self.fps_textctrl = wx.TextCtrl(self, wx.ID_ANY, "")
        self.scale_label = wx.StaticText(self, wx.ID_ANY, _("Scale:"), style=wx.ALIGN_CENTER)
        self.scale_textctrl = wx.TextCtrl(self, wx.ID_ANY, "")
        self.margin_label = wx.StaticText(self, wx.ID_ANY, _("Margin:"), style=wx.ALIGN_CENTER)
        self.x1_label = wx.StaticText(self, wx.ID_ANY, _("x1:"), style=wx.ALIGN_CENTER)
        self.x1_textctrl = wx.TextCtrl(self, wx.ID_ANY, "")
        self.x2_label = wx.StaticText(self, wx.ID_ANY, _("x2:"), style=wx.ALIGN_CENTER)
        self.x2_textctrl = wx.TextCtrl(self, wx.ID_ANY, "")
        self.y1_label = wx.StaticText(self, wx.ID_ANY, _("y1:"), style=wx.ALIGN_CENTER)
        self.y1_textctrl = wx.TextCtrl(self, wx.ID_ANY, "")
        self.y2_label = wx.StaticText(self, wx.ID_ANY, _("y2:"), style=wx.ALIGN_CENTER)
        self.y2_textctrl = wx.TextCtrl(self, wx.ID_ANY, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.file_input_button_callback, self.file_input_button)
        self.Bind(wx.EVT_BUTTON, self.file_output_button_callback, self.file_output_button)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Video2GifFrame.__set_properties
        self.SetTitle(_("Video2gif"))
        self.input_filepath_label.SetMinSize((100, 35))
        self.input_file_textctrl.SetMinSize((600, 35))
        self.file_input_button.SetMinSize((35, 35))
        self.output_filepath_label.SetMinSize((100, 35))
        self.output_file_textctrl.SetMinSize((600, 35))
        self.file_output_button.SetMinSize((35, 35))
        self.fps_label.SetMinSize((100, 35))
        self.fps_textctrl.SetMinSize((70, 35))
        self.scale_label.SetMinSize((100, 35))
        self.scale_textctrl.SetMinSize((70, 35))
        self.margin_label.SetMinSize((100, 35))
        self.x1_label.SetMinSize((35, 35))
        self.x1_textctrl.SetMinSize((70, 35))
        self.x2_label.SetMinSize((35, 35))
        self.x2_textctrl.SetMinSize((70, 35))
        self.y1_label.SetMinSize((35, 35))
        self.y1_textctrl.SetMinSize((70, 35))
        self.y2_label.SetMinSize((35, 35))
        self.y2_textctrl.SetMinSize((70, 35))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Video2GifFrame.__do_layout
        main_box = wx.BoxSizer(wx.VERTICAL)
        crop_row_box = wx.BoxSizer(wx.HORIZONTAL)
        fps_scale_res_row_box = wx.BoxSizer(wx.HORIZONTAL)
        output_row_box = wx.BoxSizer(wx.HORIZONTAL)
        input_row_box = wx.BoxSizer(wx.HORIZONTAL)
        main_box.Add(self.title_label, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        main_box.Add((20, 20), 0, 0, 0)
        input_row_box.Add(self.input_filepath_label, 0, 0, 0)
        input_row_box.Add(self.input_file_textctrl, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        input_row_box.Add(self.file_input_button, 0, 0, 0)
        main_box.Add(input_row_box, 1, 0, 0)
        output_row_box.Add(self.output_filepath_label, 0, 0, 0)
        output_row_box.Add(self.output_file_textctrl, 0, 0, 0)
        output_row_box.Add(self.file_output_button, 0, 0, 0)
        main_box.Add(output_row_box, 1, 0, 0)
        fps_scale_res_row_box.Add(self.fps_label, 0, 0, 0)
        fps_scale_res_row_box.Add(self.fps_textctrl, 0, 0, 0)
        fps_scale_res_row_box.Add(self.scale_label, 0, 0, 0)
        fps_scale_res_row_box.Add(self.scale_textctrl, 0, 0, 0)
        fps_scale_res_row_box.Add((20, 20), 0, 0, 0)
        fps_scale_res_row_box.Add((20, 20), 0, 0, 0)
        fps_scale_res_row_box.Add((20, 20), 0, 0, 0)
        fps_scale_res_row_box.Add((20, 20), 0, 0, 0)
        main_box.Add(fps_scale_res_row_box, 1, 0, 0)
        crop_row_box.Add(self.margin_label, 0, 0, 0)
        crop_row_box.Add((20, 20), 0, 0, 0)
        crop_row_box.Add(self.x1_label, 0, 0, 0)
        crop_row_box.Add(self.x1_textctrl, 0, 0, 0)
        crop_row_box.Add(self.x2_label, 0, 0, 0)
        crop_row_box.Add(self.x2_textctrl, 0, 0, 0)
        crop_row_box.Add(self.y1_label, 0, 0, 0)
        crop_row_box.Add(self.y1_textctrl, 0, 0, 0)
        crop_row_box.Add(self.y2_label, 0, 0, 0)
        crop_row_box.Add(self.y2_textctrl, 0, 0, 0)
        main_box.Add(crop_row_box, 1, 0, 0)
        self.SetSizer(main_box)
        main_box.Fit(self)
        self.Layout()
        # end wxGlade

    def file_input_button_callback(self, event):  # wxGlade: Video2GifFrame.<event_handler>
        print "Event handler 'file_input_button_callback' not implemented!"
        event.Skip()

    def file_output_button_callback(self, event):  # wxGlade: Video2GifFrame.<event_handler>
        print "Event handler 'file_output_button_callback' not implemented!"
        event.Skip()

# end of class Video2GifFrame
if __name__ == "__main__":
    gettext.install("Video2Gifapp") # replace with the appropriate catalog name

    Video2Gifapp = wx.PySimpleApp()
    Video2gif = Video2GifFrame(None, wx.ID_ANY, "")
    Video2Gifapp.SetTopWindow(Video2gif)
    Video2gif.Show()
    Video2Gifapp.MainLoop()