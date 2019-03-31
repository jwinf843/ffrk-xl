import xl2dict

myxlobject= XlToDict()
myxlobject.convert_sheet_to_dict(file_path="Soul Breaks.xlsx", sheet="First Sheet",
                                 filter_variables_dict={"User Type" : "Admin", "Environment" : "Dev"})