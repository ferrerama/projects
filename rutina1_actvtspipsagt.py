import win32com.client
import os

def actualizar_consulta_excel():
    """
    Abre el archivo de Excel, actualiza todas las consultas de datos, 
    guarda y cierra. Todo en segundo plano.
    """
    ruta_archivo = r"C:\Users\mferrera\Documents\Ventaspipsagt.xlsx"
    
    try:
        # Crea una instancia de la aplicación Excel
        excel = win32com.client.Dispatch("Excel.Application")
        excel.Visible = False  # Oculta la ventana de Excel
        
        # Abre el libro de trabajo
        libro = excel.Workbooks.Open(ruta_archivo)
        
        # Refresca todas las consultas de datos en el libro
        libro.RefreshAll()
        
        # Espera a que las consultas terminen de actualizarse
        excel.CalculateUntilAsyncQueriesDone()
        
        # Guarda y cierra el libro
        libro.Save()
        libro.Close()
        
        # Cierra la aplicación Excel
        excel.Quit()
        
        print(f"Archivo {os.path.basename(ruta_archivo)} actualizado exitosamente.")
        
    except Exception as e:
        print(f"Ocurrió un error al actualizar el archivo: {e}")
        
    finally:
        # Asegúrate de cerrar la aplicación Excel si algo falla
        if 'excel' in locals() and excel:
            excel.Quit()

if __name__ == "__main__":
    actualizar_consulta_excel()