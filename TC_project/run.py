from TC_Stand import create_app
from TC_Stand.models import Vehicle_Pic, User
from apscheduler.schedulers.background import BackgroundScheduler
import atexit, os


app = create_app()


#+---Funcões do scheduler => Apagar ficheiros desnecessários---+#
def delete_vehicle_images(app):
    with app.app_context():
        path = os.path.join(app.root_path, "static/vehicle_pics")
        filenames = []

        for (_, _, filename) in os.walk(path):
            filenames.extend(filename)

        pics = [pic.image for pic in Vehicle_Pic.query.all()]

        for file in filenames:
                if file not in pics and file != "default.jpg":
                    file_path = app.root_path + "/static/vehicle_pics/" + file
                    os.remove(file_path)

        del pics, filenames


def delete_profile_pics(app):
    with app.app_context():
        path = os.path.join(app.root_path, "static/profile_pics")
        filenames = []

        for (_, _, filename) in os.walk(path):
            filenames.extend(filename)

        pics = [user.image_file for user in User.query.all()]

        for file in filenames:
                if file not in pics and file != "default.jpg":
                    file_path = app.root_path + "/static/profile_pics/" + file
                    os.remove(file_path)

        del pics, filenames
#+------------------------------------------------------------+#


if __name__ == "__main__":
    scheduler = BackgroundScheduler()

    #+-- Faz uma limpeza das imagens a cada hora --+#
    scheduler.add_job(func=delete_vehicle_images, args=[app], trigger="interval", minutes=60)
    scheduler.add_job(func=delete_profile_pics, args=[app], trigger="interval", minutes=10)
    scheduler.start()

    atexit.register(lambda: scheduler.shutdown())

    app.run(debug=True)