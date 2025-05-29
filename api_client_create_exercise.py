from clients.authentication.authentication_client import AuthenticationClient
from clients.courses import courses_client
from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises import exercises_client
from clients.exercises.exercises_client import CreateExerciseRequestDict, get_exercises_client
from clients.files import files_client
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.users import public_users_client
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

# Инициализируем публичный клиент

public_user_client = get_public_users_client()

# Создаем пользователя

create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="Qwerty",
    lastName="Marygold",
    firstName="Yasna",
    middleName="Inkeryline"
)
create_user_response = public_users_client.create_user(create_user_request)

# Инициализируем клиент файла и курса

authentication_user = AuthenticationClient(
    email=create_user_request["email"],
    password=create_user_request["password"]
)
file_user_client = get_files_client(authentication_user)
course_user_client = get_courses_client(authentication_user)

# Загружаем файл

create_file_request = CreateFileRequestDict(
    filename="yasna.png",
    directory="courses",
    upload_file="./testdata/files/yasna.png"
)
create_file_response = files_client.create_file(create_file_request)
print(f"Create file data: {create_file_response}")

# Создаем курс

create_course_request = CreateCourseRequestDict(
    title="Yasna poops",
    maxScore=50,
    minScore=5,
    description="How to poop like a pro",
    estimatedTime="76 times",
    previewFileId=create_file_response["file"]["id"],
    createdByUserId=create_user_response["user"]["id"]
)
create_course_response = courses_client.create_course(create_course_request)
print(f"Create course data: {create_course_response}")

# Инициализируем клиент задания

exercise_user_client = get_exercises_client(authentication_user)

# Создаем задание

create_exercise_request = CreateExerciseRequestDict(
    title="This is real deal",
    courseId=create_course_response["exercise"]["id"],
    maxScore=100,
    minScore=10,
    orderIndex=5,
    description="Try exercise",
    estimatedTime="Around 3 years",
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print(f"Create exercise data: {create_exercise_response} ")

