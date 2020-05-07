from torm import Model
from torm import f
from torm.utl.Map import Map


class Record(Model):
    __config__ = "mongo"
    # __dbname__ = "test"

    id = f.Str()
    hash = f.Str()
    subject = f.Str()
    promoter = f.Str()
    recorder = f.Email()

    attachments_num = f.Int()
    mail_id = f.Str()
    group_hash = f.Str()

    status = f.Str()
    tx_status = f.Str()

    commits = f.Dict()
    group = f.EmailList()
    hashtags = f.Dict  # f.Map()

    create_at = f.Int()
    update_at = f.Int()


def test_insert_one():
    commits = {'user_id': 'some thing'}

    hashtags = {'1': ['']}
    record = Record({
        "hash": '12',
        "recorder": "thhk06@163.com",
        "subject": "test",
        "hashtags": hashtags,
        "group": ["thhk06@163.com", "kai.he@taraxa.io"],
        "commits": commits
    })

    # for k in record:
    #     print(k)
    # a = Map(record)
    # print(a)

    # for i in record:
    #     print(record[i])

    # record = {
    #     "id": '5eacf4e81e57fa47f0a732c4',
    #     "hash": '12',
    #     "recorder": "thhk06@163.com",
    #     "subject": "test",
    #     "hashtags": hashtags,
    #     "group": ["thhk06@163.com", "kai.he@taraxa.io"],
    #     "commits": commits
    # }

    r = Record.InsertOne(record)
    print(r)


def test_find():
    # hash = "0x123"
    # record = Record.FindOne(hash)
    record = Record.FindOne()
    print(record.pretty())
    # print(record.to_map())


def test_find_many():
    records = Record.FindMany()
    print(records)


def test_update_one():
    r = Record.UpdateOne(hash, {'subject': 'test5'})
    print(r)


# test_find()
# test_insert_one()

# print(r)
# print(Record.__dict__.keys())

# r = Record.where({'id': '5ead0d7f34e0b4dddeb234e3'}).get()
#   r = Record.where('id', '=', '5ead0d7f34e0b4dddeb234e3').first()
# print(r)
# test_find_many()

test_find()
